# Permission in linux filesystetm

```sh
-rwxrw-r--     # <- User, Group, Others    <- they are in this order
# Read, write execute for user
# Read, write for Group
# Read for other.

drwxrw-r--   #<- the d means that the thing is a directory

```

## Changing Permissions

#### words that makes sense:
- a <- all
- u <- user
- g <- group
- o <- others

```sh
chmod a+x file.txt
```

#### Numbers that makes sense:
- 0 <-not permission
- 1 <- execute only
- 2 <- write only
- 4 <- read only

```sh

chmod 751 file.txt

# Read, write, execute to owner ( 4 + 2 + 1)
# Read, execute to group ( 4 + 1)
# execute to others
```