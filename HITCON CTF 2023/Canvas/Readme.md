# Overview
This is a tricky XSS challenge.
I failed at this challenge but learned a lot.

# Solution
This is a website that allows you to run arbitrary Javascript code in a sandboxed Javascript worker.
User code is passed to a function that has overwritten nearly everything in `window` object, and `this` is also overwritten by `fn.apply()`.

But `this` in javascript is a strange thing, its value depends on where it is called.
For a better understanding, better go read [Huli's blog](https://blog.techbridge.cc/2019/02/23/javascript-this/).

In conclusion, even if `this` is overwritten, we just need to create a new scope by creating a new non-arrow function to retrieve `this`, which is the global scope of worker.

With `this`, we can call the overwritten methods and attributes!
But in a worker, things like `alert` does not exist.
Therefore, we need to find a way to escape the worker.

In the `main.js`, we can see that it loaded `worker.js` and add a message event listener to it.
If we run `postMessage({type: "error", content: "blabla"})`, the content will be throw into `setHTML`
`setHTML` does some XSS prevention by sanitizing dangerous attributes and tags, but it's not that safe, because tags like `<meta>` still works, and we can use it to redirect or do something else.

And in the worker global scope, we can also access `Blob` and `URL`. This is a new trick I learned in this challenge.
You can create a blob object and specified it's content and MIME type, and that means, we can create a blob page with custom html!
In a blob url page, even if the URL starts with "blob:", it's still same-origin to the original website. So we can access same-site cookies and localStorage Items!

But we can't actually execute arbitrary code in blob page, because blob page inherits CSP from original page.
The only allowed rule is `unsafe-eval`, so we need to find some gadget to exploit this.
The `worker.js` in original site does eval our code in a worker context, so we can't call dangerous thing there.
But that only happens if it's loaded as worker!
We can simply use `<script src="">` to load the worker to eval our code outside of worker this time.

{% note %}
There are two `postMessage`, one is in worker object, another is a method in `Window`.
The one we're using here is the latter, since we're not in worker anymore.
{% endnote %}

We just need to create a canva to make it not crash, and `postMessage` again to trigger code eval to execute XSS!
Again, this is kinda new to me, since we need to `postMessage` manualy to achieve XSS, we can't just do that in the blob page.
But we can actually do that in our own site and use iframe to do that!

{% note %}
Usually, when user's current site and iframe's site isn't same-origin, you cannot access the attributes, objects, methods from the website in iframe.
But there are few exceptions, and one is `postMessage`, since `postMessage` is exactly designed to do such things.
{% endnote %}


The full payload can be found in maple3142's github repo.

## Exploit chain
1. Recover `this` by ceating new non-arrow function.
2. Escape worker by using `Blob` and `URL` and abusing `setHTML` to redirect to blob page.
3. Bypass CSP by loading `worker.js` in <script>, and then we can abuse the gadget to execute JS code.
4. Chain everything above. Use iframe to create a blob page and redirect to it, and then use `iframe.contentWindow` to access the blob page to execute `postMessage`.







