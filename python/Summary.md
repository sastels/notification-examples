
## Notify is easy to use (hopefully!)

- You can use the api with simple POSTs and GETs.
- GovUK maintains libraries that work(ish) with Canadian Notify too.

## Keep your api key secure!

- Not in the code.
- Use approved secrets management procedures / tools.
- We don't want criminals using your service to attack Canadians.

## Always check the response of a POST

- You might have made a mistake.
- Notify might be rate limiting you.
- Notify might be having problems :O

## You should also check the end status of messages!
- Lots of errors in email addresses and phone numbers.
- Text messages sometimes just disappear inside the provider.


## Be able to handle Notify returning error messages
- Retry failed messages after a delay.
- Rate limit your POSTs to Notify if need be.
- Be able to deal with your message not reaching the user (ex: bad email address).
- Remove bad phone numbers and email addresses from your mailing lists.

## Feel free to ask for new features through our contact form
- This is the main way we find out what you folks want out of Notify.

## We are here to help you
- Don't spin your wheels for too long, reach out to us with any problems.

