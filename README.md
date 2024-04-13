# How to run this code

**Step 1**: Add `yourlieapril.test` domain to `hosts` file (`/etc/hosts` on Mac/Linux) by append this line at file's bottom:

```
127.0.0.1       yourlieapril.test
```

**Step 2**: Build docker

```
cd docker
./exec build
```

**Step 3**: Install evironments and migrate to database

```
./exec up
./exec makemigrations
./exec migrate
```

**Step 4**: Run web's web server

```
./exec bserver
```

Then visit: `https://yourlieapril.test/`

# Edit by Luong Van Hoang / give me a coffee( 0388347846 / Liobank ) Thank's a lot :>>
