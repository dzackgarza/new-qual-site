# E-SS3.PR-4 — solution for installation

Slice 1 of swarm smvy31u3e. Card: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-4.md`
(Stein–Shakarchi, *Complex Analysis*, Chapter 3, §9, Problem 4*, printed page 110 = PDF page 129).

## Files

- `solution-block.md` — the block to **append** verbatim to the card. Nothing else is needed;
  the card has no solution block at all.
- `E-SS3.PR-4.with-solution.md` — card + that block, i.e. the finished card, for convenience.

I did not touch anything under `corpus/`; installation is a human step.

## What is proved

The whole problem: if $\Omega$ is a bounded region, $L$ a line meeting $\Omega$, $\Omega\cap L=I$ an
interval, and $\Omega_l,\Omega_r$ the two halves are simply connected, then $\Omega$ is simply
connected. "Simply connected" is used exactly as Chapter 3, §5 defines it (any two curves with the
same endpoints are homotopic), and the conclusion is proved in that form.

Nothing is left incomplete, and no hypothesis is weakened. The boundedness of $\Omega$ is *not used*
by the argument (the proof is written so as to make that visible), so the statement also holds for
unbounded $\Omega$; only "$I$ is an interval" and the simple connectivity of the two halves enter.

## Shape of the argument

Normalize $L=\mathbb{R}$ and write $I$ for the interval $\Omega\cap\mathbb{R}$, which is convex.

1. Elementary homotopies of concatenations (inverse pairs, constant curves, associativity,
   composition, reparametrization).
2. Every curve in $\Omega$ is homotopic, endpoints fixed, to a polygonal curve. The proof is the
   covering argument of the book's Theorem 5.1 (ch. 3, §5) plus uniform continuity and
   straight-line homotopies inside the balls.
3. Every polygonal closed curve is freely homotopic to one with no vertex on $L$ and no side
   parallel to $L$, so it crosses $L$ finitely often and transversally: perturb the vertices by
   $i s_k$ and choose $s_k=t^{k+1}$ for a small $t$ outside the finitely many bad values.
4. **Crosscut lemma (the heart).** If $p,q\in I$ and $A$ is a curve from $p$ to $q$ whose interior
   lies in one half (say $\Omega_l$), then $A*s^{-1}$ is null-homotopic, where $s=[p,q]$. Proof:
   take a convex tube $W$ around $[p,q]$ inside $\Omega$; cut $A$ near its two ends into
   $A=\alpha*\mu*\gamma$ with $\alpha,\gamma\subseteq W$ and $\mu\subseteq\Omega_l$; the two paths
   $\gamma*s^{-1}$ and $[a_1,a_0]*\alpha^{-1}$ run inside the convex set $W$ between the same two
   points, hence are homotopic there; $\mu*[a_1,a_0]$ is a closed curve in the simply connected
   $\Omega_l$, so it is null-homotopic, and conjugating by $\alpha$ finishes.
   Corollary: $A\simeq s$ with endpoints fixed.
5. A closed polygon crossing $L$ splits into subarcs $A_1,\dots,A_m$ with interiors in one half
   (the wrap-around subarc is dealt with: both of its pieces have the off-line base point in their
   closure). Hence $P\simeq s_1*\cdots*s_m$, which lies in the convex set $I$ and is therefore
   null-homotopic.
6. A closed curve that is freely null-homotopic is null-homotopic at its base point (explicit
   three-piece homotopy), so every closed curve in $\Omega$ is null-homotopic, and then
   $\gamma_0*\gamma_1^{-1}$ null-homotopic gives $\gamma_0\simeq\gamma_1$ rel endpoints.

Book results cited: the definition of simple connectivity and Example 1 of Chapter 3, §5 (printed
pp. 93–96), i.e. the linear-interpolation homotopy — applied verbatim to any convex set — and the
covering argument from the proof of Theorem 5.1 there.

## Verification run

All in this repository, nothing written under `corpus/`:

- `pandoc -f markdown -t html --lua-filter ~/.pandoc/filters/lamport_proof.lua` on
  card+block: exit 0, no filter error; the block parses as 8 steps with step 5 carrying
  substeps 5.1–5.4, and all 15 `pf-ref` links resolve.
- The per-card checks of `tools/qualc/authoring.py`, run on card+block from a scratch copy
  (`card_header` schema + fence balance, `raw_notation`, `RAW_BLACKBOARD`,
  `BACKSLASH_DELIMITER`, `unread_math_errors`): clean. (`just check-card` itself refuses paths
  outside `corpus/`, which is why the checks were driven directly.)
- `python3 tools/check_macros.py` on the block: all control words defined.
- Every math snippet of the block (6 display, 427 inline) compiles under `pdflatex` with
  `amsmath`/`amssymb` and the four macros it uses.

## One correction for the card's audit note

The front matter of the card records the statement as read from "PDF page 128". It is on printed
page 110 = **PDF page 129**; PDF page 128 (printed 109) ends with problem 1(g). The transcription
itself is correct — compare `pdftotext -layout -f 129 -l 129`.
