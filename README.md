# README

## Prerequesites

Install [chromedriver](https://sites.google.com/chromium.org/driver/) into this directory or somewhere else in `PATH`.

## Ipython Notebooks in Git

Remeber to put the following filter into the repo's config:

```
[filter "nbstrip_full"]
        clean = "\"jq\" --indent 1 \
                '(.cells[] | select(has(\"outputs\")) | .outputs) = []  \
                | (.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
                | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
                | .cells[].metadata = {} \
                '"
        smudge = cat
        required = true
```

And also

```
*.ipynb filter=nbstrip_full
```

into `.gitattributes`.

Install [jq](https://stedolan.github.io/jq/) somewhere into `PATH`, if necessary.
