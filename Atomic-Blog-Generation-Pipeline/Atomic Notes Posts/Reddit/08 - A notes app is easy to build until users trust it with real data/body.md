The UI for a notes app isn't the part that worries me most anymore.

The hard parts are the ones users may never see:

- the app gets killed during sync
- the network disappears after an upload starts
- duplicate retries
- conflicting edits from two devices
- stale versions
- deleted notes coming back
- encrypted and unencrypted records mixing
- migrations between app versions
- keeping unsynced local work safe
- avoiding double charges for failed operations

Atomic Notes has forced me to think far more about failure states than happy paths.

For people who have built local first or sync-heavy apps: which failure mode surprised you most?
