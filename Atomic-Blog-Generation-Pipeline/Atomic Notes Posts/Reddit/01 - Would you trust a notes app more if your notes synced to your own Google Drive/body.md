I'm building **Atomic Notes**, a local first notes app for Android. Its code is public on GitHub under a source-available license.

One architectural decision I keep coming back to is storage ownership.

Instead of treating the app's own cloud database as the permanent home of your notes, Atomic Notes keeps notes on the phone first and syncs them as files into a private folder in your own Google Drive. It uses the `drive.file` scope, so the app can only see the files it created.

The backend still handles sign-in, sync coordination, versions, sessions, Atomic Energy (the sync allowance) and metadata like note ids and timestamps. It never stores note text. With the encryption vault off, note text passes through the server on its way to your Drive. With the vault on, each note is encrypted on the device with AES-256-GCM first, so only ciphertext travels.

I'm curious how people here think about this model.

Would user owned cloud storage make you trust a notes app more? Or would you still prefer self-hosting, WebDAV, Syncthing or device-only notes?

Project: https://atomic-notes-community.vercel.app/
Code: https://github.com/DevBehindYou/Atomic-Notes-App-V0.2

Negative feedback is welcome. I'm trying to learn where this design is strong and where it adds complexity for no good reason.
