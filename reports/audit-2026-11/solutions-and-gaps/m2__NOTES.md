# E-SSA.PR-5 — deliverable notes (member m2, swarm smvy31u3e)

## The deliverable

`E-SSA.PR-5.solution.md` is the complete `::: {.solution}` block, ready to append at the end of

    corpus/collections/SRC-TEXT-SS03/appendix-a-problems/E-SSA.PR-5.md

(i.e. directly after that card's `::: {.exercise}` block). Nothing under `corpus/` was modified; the
block is checked to parse with `pandoc -f markdown+fenced_divs+tex_math_dollars+pipe_tables` into a
single `Div ("",["solution"],[])` with 21 display equations and one pipe table. Only user macros that
exist in `vocabularies/macros.json` are used (`\HH`, `\ZZ`, `\abs`, `\norm`, `\eps`, …); everything
else is standard MathJax.

The card is problem 5\* of Appendix A §5 (Stein–Shakarchi, *Complex Analysis*, printed p. 343 =
PDF page 362; §4 and Theorem 4.1 are printed pp. 334–341 = PDF pages 353–360).

## What the block proves, and what it refuses to prove

Proved in full:

1. **Theorem 2** — the transformation at an arbitrary rational point $p/q$:
   $f(\xi+p/q)=\omega_{p/q}(\xi q/i)^{1/2}e^{\pi i/(12q^2\xi)}e^{\pi i\xi/12}f(-1/(q^2\xi)-p'/q)$,
   with $|\omega_{p/q}|=1$, $\omega_{p/q}^{24q}=1$, independent of the choice of $p'$.
   Proved from (24) + $f(z+1)=f(z)$ exactly as the book says one can, by first proving
   **Lemma 1** (the multiplier of $\eta$: $\eta(\gamma z)=\varepsilon(\gamma)(cz+d)^{1/2}\eta(z)$ with
   $\varepsilon(\gamma)\in\mu_{24}$ for $\gamma\in SL_2(\ZZ)$, $c>0$), by Euclidean descent on $c$
   from the two cases the book does supply ($\eta(z+1)$, Prop. 1.9 of Ch. 10).
2. **Theorem 3** — the contribution of the point $p/q$:
   $c_{p/q}\frac{1}{2\pi\sqrt2}\frac{d}{dn}[e^{(K/q)\lambda}/\lambda]$ with
   $c_{p/q}=\sqrt q\,e^{-2\pi inp/q}\omega_{p/q}$, so $|c_{p/q}|=\sqrt q$, obtained by redoing §4's
   second computation with $(s,\mu)\mapsto(s/q,\mu/q)$; the constant $\frac1{2\pi\sqrt2}$ is derived
   from scratch ($\mu_q^{1/2}\sqrt{\pi/s_q}=\lambda^{-1}/\sqrt2$ because $K\sqrt6=2\pi$), and the
   $q=1$ case is checked to reproduce Theorem 4.1(ii) and Theorem 4.1(i) exactly.
3. A factor-by-factor table (what $\omega$, $(\xi q/i)^{1/2}$, $e^{\pi i/(12q^2\xi)}$,
   $e^{\pi i\xi/12}$, $f(-1/(q^2\xi)-p'/q)$ each contribute), including the observation that
   $e^{\pi i\xi/12}$ is exactly the source of the shift $n\mapsto n-\tfrac1{24}$.

Deliberately **not** proved, and flagged as such in the block (section 4):

* the book's last sentence, that the series over all $p/q$ "when suitably modified" converges and is
  an exact formula. The block lists the four things a proof would need: the multiplier $\varepsilon$
  in closed form (Dedekind sums, not in the book), the Farey dissection with uniform estimates, a
  demonstration that the book's own error bound $O(e^{Kn^{1/2}/2})$ cannot even see the $q\ge2$ terms
  (it cannot: for $q\ge2$ the local term is $\le e^{K\lambda/2}$), and Rademacher (1937).

So the block is complete for the two assertions the exercise makes and explicitly incomplete for the
third. This is the reading required by the task ("leave the block marked incomplete rather than
filling it with a plausible argument").

## Two corrections to the printed statement (both proved in the block)

The book prints (PDF p. 362, `pdftotext -raw`, verbatim with its own OCR spacing)

    f(z − p/q) = ω_{p/q} √(zq/i) e^{iπ/(12zq²)} e^{−iπz/12} f(−1/(zq²) − p'/q),   pp' ≡ 1 mod q,

and "Here ω_{p/q} is an appropriate 24th root of unity."

* **The sign.** With the printed $e^{-\pi iz/12}$ no constant $\omega$ works: taking $q=1$, $p=p'=1$
  gives $f(z-p/q)=f(z)$ and $f(-1/(zq^2)-p'/q)=f(-1/z)$, so the printed identity would force
  $\omega_{1/1}(z/i)^{1/2}e^{\pi i/(12z)}e^{-\pi iz/12}f(-1/z)=f(z)$, while (24) gives the same with
  $e^{+\pi iz/12}$; hence $\omega_{1/1}=e^{\pi iz/6}$, not a constant. The exponent must be
  $e^{+\pi i\xi/12}$.
* **The variable.** The printed formula uses the same letter $z$ in $f(z-p/q)$ and inside
  $(zq/i)^{1/2}$, $e^{\pi i/(12zq^2)}$, $e^{-\pi iz/12}$. The consistent reading is that everything on
  the right is evaluated at the shifted variable $\xi=z-p/q$; with the unshifted $z$ the formula is
  false already for $q=1$.
* **The order of the root of unity.** The derivation gives $\omega_{p/q}\in\mu_{24q}$ only, since the
  factor $e^{\pi i(p+p')/(12q)}$ is a $24q$-th root in general. Whether it is a $24$th root is a
  Dedekind-sum congruence which the book neither states nor proves. In particular my numerics give
  $\omega_{1/3}$ of order $36$, $\omega_{1/4}$ of order $48$, $\omega_{1/5}$ of order $10$ — so in this
  normalization the printed "24th root" is not correct as it stands. The block says only what is
  needed downstream ($|\omega_{p/q}|=1$).

## Numerical checks (scripts in `checks/`, reproducible)

`checks/check_transformation.py` (needs `mpmath`): computes
$\omega=\text{LHS}/\text{RHS}$ of Theorem 2 from the Euler product
$f(z)=\prod_{n\ge1}(1-e^{2\pi inz})^{-1}$ at three different points $\xi$ for every $p/q$ with
$q\le7$. Output: $|\omega|-1<10^{-40}$, constancy in $\xi$ to $10^{-25}$, $\omega^{24q}=1$ to
$10^{-48}$, and the same value for $p'$ and $p'+q$.

`checks/check_omega_order.py`: values $\omega_{p/q}$; $|\omega^{24}-1|$ is $0$ for $0/1,1/2,2/5$ and
nonzero for $1/3$ ($1.73$), $1/4$ ($2$), $1/5$ ($1.90$), $1/6$ ($1.73$), $1/7$ ($1.56$).

`checks/check_local_constant.py`: integrates the local model over the Farey arc
$|\xi|\le 1/(2q\sqrt n)$, $\operatorname{Im}\xi=\delta=(4\sqrt6\sqrt n)^{-1}$, and compares with
$\omega\frac{1}{4\sqrt3}q^{-1/2}\lambda^{-2}e^{K\lambda/q}$ ($\omega=1$ set in both). Ratios:
$n=400$: $0.9805$ ($q=1$), $0.9610$ ($q=2$); $n=900$: $0.9870$ ($q=1$), $0.9740$ ($q=2$),
$0.9631$ ($q=3$). The deviation shrinks like $n^{-1/2}$, as the $1+O(n^{-1/2})$ in Theorem 3 predicts,
and the $q$-scaling ($q^{-1/2}$, $e^{K\lambda/q}$) is confirmed.

These checks are *not* part of the proof in the block; the block is analytic throughout. They were
used to catch two algebraic slips of my own (a wrong power of $q$ in one intermediate display, and the
missing $\omega$ in another) before writing the final text.

## Honest status

* The two substantive assertions of the exercise (transformation; contribution) are proved in the
  block, with the corrections above, and nothing in it is asserted on the book's authority alone:
  every citation is to a numbered item — (23), (24), (25), (26)--(28), Theorem 4.1(i)(ii),
  Proposition 1.9 and Theorem 2.1 of Chapter 10, and Proposition 2.1 (Laplace's method).
* The exact-formula sentence is not proved, here or in the book; section 4 of the block says exactly
  what is missing.
* No claim is made about the value of $\omega_{p/q}$ beyond $|\omega|=1$, $\omega^{24q}=1$ (proved) and
  the numerical values above.
