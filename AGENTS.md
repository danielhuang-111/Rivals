# Project instructions

This is a single-file browser game: `index.html` (Three.js loaded from a CDN, no build step).

## Always push changes

After any change to this project, commit and push it to GitHub:

```
git add -A
git commit -m "<short description of the change>"
git push
```

- Remote: `origin` -> `git@github.com:danielhuang-111/Rivals.git`
- Branch: `main` (tracked)
- Authentication is configured via SSH (`~/.ssh/id_ed25519`).

## Testing

Serve the folder locally and check the page/console, e.g.:

```
python3 -m http.server 8731
```

Then open `http://127.0.0.1:8731/index.html`.
