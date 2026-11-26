# Worktrees from before this rule

`git worktree list` reports only the main checkout, and `test-commit` runs `_no-worktrees`.
If a worktree from before this rule is found, it is not debris and must not be removed on
sight: another stream's authoring is live until three readings say otherwise, taken
immediately before the removal and never carried over from an earlier survey.

The three readings, in order, are: 1. the worktree is clean; 2. its commits are reachable
from `main`; 3. no process uses it.

```bash
git -C PATH --no-optional-locks status --short
git merge-base --is-ancestor "$(git -C PATH rev-parse HEAD)" HEAD
pgrep -a -f PATH
```

Reading 1 fails on any output at all — staged or unstaged, tracked or untracked. An
uncommitted card is somebody's unbanked authoring, and a `.orig` file beside it is the
evidence of a merge they are still resolving. Reading 2 asks whether every commit on
that worktree's branch is already in `main`; run it from the main checkout, whose
`HEAD` is the reference. Reading 3 discards the checking shell's own PID, and
`pgrep -f` matches on substring, so a probe for `sp19` also matches `sp19-audit2` —
read the command lines it prints rather than counting them.

When all three pass:

```bash
git worktree remove .worktrees/<name>
git worktree prune
```

When any one fails, leave it in place and report it. Re-take all three for each
worktree at the point of removal rather than acting on a list. Worktrees outside the
repository are outside this rule; report them and do not remove them.
