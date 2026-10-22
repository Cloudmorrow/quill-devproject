# DevProject

A Quill for [Cloudmorrow](https://github.com/Cloudmorrow/cloudmorrow): your
software projects, each with its git repository, its notes, a board, and
its `.env` secrets, on every machine you work on.

```
cd ~/code/myapp
cm devproject init                 # a project, and every .env file here into its vault
cm devproject list                 # your projects

# on another machine
cm devproject clone myapp          # the repository, then its .env files written back
cm devproject update               # in the folder: git pull, then the .env files from the vault

cm devproject secrets                                  # its environments, and the file each is
cm devproject secrets import -e local -f .env          # one file in (or every file, without -e and -f)
cm devproject secrets export myapp -e prod -f .env.prod  # one environment out, from anywhere
```

- **One environment per file.** `.env.prod` is `prod`, `.env.local` is
  `local`, `.env` is `local` (or `default` when there is a `.env.local`
  beside it). Each environment is written back to the file it was read
  from. `.env.example` and other templates, and any file git tracks, are
  left alone.
- **The secrets are Cloudmorrow's.** They go into the Secrets manager, in a
  vault named after the project (`myapp`), sealed under the server's key,
  and `cm secret -v myapp …` reaches them as well. Installing DevProject
  installs Secrets.
- **Nothing local is lost.** `update` never takes a key out of a `.env` file
  that the vault does not have: that file is left as it is and named, until
  you `secrets import` it or pass `--force`. Files are written mode 600.
- **The same on every surface.** In the web app and on the phone a project's
  sheet lists its environments: save each as its `.env` file, or read one
  in; the Project secrets tab has Import .env and Export .env. In the
  terminal app, `i` inits a folder, `u` updates, `c` clones and `m` imports,
  on the project under the cursor.
- **A board per project:** To Do, Doing, Done.

## What it adds to your Cloudmorrow

| | |
| --- | --- |
| Datamodels | extends the foundational `project` with `devproject.repo`, `devproject.vault` and `devproject.env_files`; introduces `devproject.card` (the board); uses `secret` |
| Screens | Projects (a list of projects: the vault, repository and env files bound), Board (a board per project), Project secrets (by vault and environment) |
| Requires | the Secrets Quill |
| Jobs, datasets, services, webhooks, APIs | none |

It contains no code: everything above is declared in [`quill.toml`](quill.toml).
What a list of projects does on your machine is Cloudmorrow's own
(`checkout.py` in the core), the same for every Quill that binds a vault.

## Working on it

See [CLAUDE.md](CLAUDE.md) and the skills in `.claude/skills/`. In short:

```
uv sync                  # .venv with Cloudmorrow and pytest
cm quill check           # the manifest, as a server would install it
cm quill test            # tests/, against the real record store and gate
cm quill dev --local     # a throwaway server here, reinstalled as you save
```

## Licence

AGPL-3.0-or-later.
