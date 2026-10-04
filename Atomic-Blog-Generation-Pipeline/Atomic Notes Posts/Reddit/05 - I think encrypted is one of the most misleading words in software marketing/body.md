A lot of apps say:

"Your data is encrypted."

But that can mean very different things:

- HTTPS while data is moving
- encrypted disks on the server
- a server database encrypted with a provider-controlled key
- client-side encryption
- actual end to end encryption

Those aren't the same security model.

In Atomic Notes, the encrypted vault is optional and off by default. With it off, notes are protected by HTTPS on the way and by your Google account in your Drive. With it on, a key derived on your phone from a six-word phrase encrypts each note with AES-256-GCM before it syncs, so the server and Drive only ever hold ciphertext.

I'm trying to keep the docs explicit about what protection exists in each mode, instead of saying "encrypted" and letting people assume the strongest version.

Should software products be expected, at least culturally, to explain **who controls the decryption key** whenever they advertise encryption?
