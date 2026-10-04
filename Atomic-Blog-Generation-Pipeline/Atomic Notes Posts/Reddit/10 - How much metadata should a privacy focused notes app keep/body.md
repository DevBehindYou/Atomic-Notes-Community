This is something privacy discussions often skip.

Even when note content is encrypted, a service may still need or see some metadata:

- account ID
- timestamps
- sync versions
- operation IDs
- device or app version
- session data
- usage needed for rate limiting or billing

Here's everything the Atomic Notes server keeps today: your Google account ID, email and name, the username you choose, Energy and coin balances with their history, each note's id, type, timestamps, pinned and deleted flags and Drive file id, your Google tokens (encrypted with AES-256-GCM), which announcements you've read, and a 30-day log of security events like sign-ins. It never stores note titles or text.

The challenge is deciding what's truly necessary versus merely convenient.

For privacy-focused software, where should the line be? Is "collect only what the feature can't work without" a realistic standard?
