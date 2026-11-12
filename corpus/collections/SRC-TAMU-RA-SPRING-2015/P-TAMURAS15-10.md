---
schema: qual/card@1
id: P-TAMURAS15-10
kind: problem
title: Extending an equivalent norm from a subspace of a normed space
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Dual Spaces
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-10-31
  note: >-
    Checked against assets/attachments/j15.pdf, Spring 2015 problem 10, whose
    text reads "with a subspace Y" and omits any closedness hypothesis.
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    Statement (i) is false without a closedness hypothesis. Take X = C[0,1] with
    the sup norm, Y the polynomials, and ||y||_1 = 2||y||, so K = 2 satisfies the
    bracket. Every phi in S is bounded for 2||.|| on X and vanishes on the dense
    subspace Y, hence is zero, so ||x||_2 = 0 for every x and ||.||_2 is not a
    norm. The statement now requires Y closed, which is what the proof of (i)
    uses. That replacement was at the time of writing a proposed correction,
    the counterexample refuting the printed claim without establishing the
    corrected one; it is now certified, see the solution-reviewed event below
    and <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/Tamuras15_10.lean>.
- event: solution-written
  by: claude
  date: 2026-10-31
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Certified. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/NormExtension.lean> proves that for a closed subspace Y and
    x not in Y a functional of norm at most one vanishes on Y and not at x;
    <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/Tamuras15_10.lean> proves the corrected statement in full: for a second
    norm n on Y with n y <= K ‖y‖ and ‖y‖ <= K n y, the supremum of |phi x| over the
    set S of the problem is nonnegative, vanishes only at 0, is homogeneous and
    subadditive, agrees with n on Y, and satisfies K^-1 ‖x‖ <= sup <= K ‖x‖. No sorryAx.
    The printed statement and the counterexample stay on the card.
- event: source-corrected
  by: claude
  date: 2026-11-06
  note: >-
    Correction to the two stale statements above about certification. The
    source-corrected event said that no machine-checked certificate of the
    corrected statement exists, and the closing remark said the closedness
    replacement was proposed and not certified; both were true when written and
    are false now. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/Tamuras15_10.lean> was elaborated in this project
    on 2026-11-06 and proves corrected_statement, with #print axioms reporting
    only propext, Classical.choice and Quot.sound for it and for the lemmas it
    depends on. Both stale sentences now point at that file and its theorem
    name.
---

::: {.problem}
Let $(X,\norm{\cdot})$ be a normed vector space with a closed subspace $Y$, and let $\norm{\cdot}_1$ be another norm on $Y$ that satisfies
$$
\frac1K\norm{y}_1\le\norm{y}\le K\norm{y}_1,\qquad y\in Y,
$$
where $K>1$ is a fixed constant.
Define $S$ to be the set of linear functionals $\phi:X\to\RR$ satisfying
$$
\abs{\phi(y)}\le\norm{y}_1\quad (y\in Y)
\qquad\text{and}\qquad
\abs{\phi(x)}\le K\norm{x}\quad (x\in X).
$$
Prove the following statements:

(i) $\norm{x}_2\coloneqq\sup\{\abs{\phi(x)}:\phi\in S\}$ defines a norm on $X$.

(ii) For $y\in Y$, $\norm{y}_1=\norm{y}_2$.

(iii) The norms $\norm{\cdot}$ and $\norm{\cdot}_2$ are equivalent on $X$.
:::

::: {.solution}
Use the Hahn--Banach theorem in the form: a linear functional on a subspace $Y\subseteq X$ that is dominated there by $q\|\cdot\|$, for a seminorm $q$, extends to a linear functional on $X$ still dominated by $q\|\cdot\|$.
The set $S$ is nonempty, since $0\in S$, and it is symmetric, since $-\varphi\in S$ whenever $\varphi\in S$.

::: pf

::: {.pf-step #functional-on-y}
For every $y\in Y$ there is $\varphi\in S$ with $\varphi(y)=\norm{y}_1$.

::: pf-proof
Define $f$ on the line $\RR y$ by $f(ty)=t\norm{y}_1$; then $\abs{f(ty)}=\norm{ty}_1$, so $f$ is dominated by $\norm{\cdot}_1$ on its domain.
By Hahn--Banach $f$ extends to $g\in Y^*$ with $\abs{g(y')}\le\norm{y'}_1$ for all $y'\in Y$.
The hypothesis gives $\norm{y'}_1\le K\norm{y'}$, so $g$ is dominated by $K\norm{\cdot}$ on $Y$ and extends by Hahn--Banach to $\varphi\in X^*$ with $\abs{\varphi(x)}\le K\norm{x}$ for all $x$.
Then $\varphi$ satisfies both conditions defining $S$, and $\varphi(y)=g(y)=\norm{y}_1$.
:::

:::

::: {.pf-step #functional-outside-y}
For every $x\in X\setminus Y$ there is $\varphi\in S$ with $\varphi(x)\ne0$.

::: pf-proof
Since $Y$ is closed and $x\notin Y$, the number $d=\inf_{y\in Y}\norm{x-y}$ is positive.
Let $Z=Y+\RR x$, a subspace on which each element is uniquely $y+tx$ with $y\in Y$ and $t\in\RR$, and define $\psi(y+tx)=t$.
For $t\ne0$ one has $\abs{\psi(y+tx)}=\abs t\le\norm{y+tx}/d$, and for $t=0$ it vanishes; hence $\abs{\psi(z)}\le d^{-1}\norm z$ on $Z$, and $\psi$ is linear with $\psi(x)=1$.
By Hahn--Banach $\psi$ extends to $\varphi\in X^*$ with $\abs{\varphi(x')}\le d^{-1}\norm{x'}\le K\norm{x'}$ for all $x'$, and $\varphi$ vanishes on $Y$.
So $\varphi\in S$ and $\varphi(x)=1\ne0$.
:::

:::

::: {.pf-step #part-i}
(i) $\norm{x}_2\coloneqq\sup\{\abs{\varphi(x)}:\varphi\in S\}$ defines a norm on $X$.

::: pf-proof
The supremum is finite, because every $\varphi\in S$ satisfies $\abs{\varphi(x)}\le K\norm x$, and it is nonnegative.
For $t\in\RR$ one has $\{\abs{\varphi(tx)}\}=\abs t\{\abs{\varphi(x)}\}$, so $\norm{tx}_2=\abs t\norm{x}_2$.
For $x,x'\in X$ and each $\varphi\in S$, the triangle inequality in $\RR$ gives $\abs{\varphi(x+x')}\le\abs{\varphi(x)}+\abs{\varphi(x')}\le\norm{x}_2+\norm{x'}_2$, so $\norm{x+x'}_2\le\norm{x}_2+\norm{x'}_2$.
Finally let $x\ne0$. If $x\in Y$ then step [](#functional-on-y){.pf-ref} gives $\varphi(x)=\norm{x}_1>0$, since $x\ne0$ and $\norm{\cdot}_1$ is a norm; if $x\notin Y$ then step [](#functional-outside-y){.pf-ref} gives $\varphi(x)\ne0$.
So $\norm{x}_2>0$, and $\norm{\cdot}_2$ is a norm.
:::

:::

::: {.pf-step #part-ii}
(ii) For $y\in Y$, $\norm{y}_1=\norm{y}_2$.

::: pf-proof
Each $\varphi\in S$ satisfies $\abs{\varphi(y)}\le\norm{y}_1$, so $\norm{y}_2\le\norm{y}_1$.
Step [](#functional-on-y){.pf-ref} exhibits $\varphi\in S$ with $\varphi(y)=\norm{y}_1$, so $\norm{y}_2\ge\norm{y}_1$.
:::

:::

::: {.pf-step #part-iii}
(iii) The norms $\norm{\cdot}$ and $\norm{\cdot}_2$ are equivalent on $X$.

::: pf-proof
Every $\varphi\in S$ satisfies $\abs{\varphi(x)}\le K\norm x$, so $\norm{x}_2\le K\norm x$.
Conversely let $x\ne0$ and choose by Hahn--Banach a functional $g\in X^*$ with $\norm{g}=1$ and $g(x)=\norm x$; then $\varphi\coloneqq g/K$ satisfies $\abs{\varphi(x')}\le\norm{x'}/K\le K\norm{x'}$ on $X$, and $\abs{\varphi(y)}\le\norm y/K\le\norm{y}_1$ on $Y$ by the hypothesis, so $\varphi\in S$.
Hence $\norm{x}_2\ge\abs{\varphi(x)}=\norm x/K$, and with the other inequality,
$$
\frac1K\norm{x}\le\norm{x}_2\le K\norm{x}
$$
for every $x\in X$.
:::

:::

:::
:::

::: {.remark}
The paper prints problem 10 with a subspace $Y$ and no closedness hypothesis.
As printed, statement (i) fails: for $X=C[0,1]$ with the sup norm, $Y$ the polynomials and $\norm y_1=2\norm y$, every $\varphi\in S$ is bounded and vanishes on a dense subspace, so $S=\{0\}$ and $\norm x_2=0$ for every $x$.
The statement above adds closedness, and that replacement is certified: <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/Tamuras15_10.lean> proves `corrected_statement`, which says that for `Y` closed the supremum norm of the problem is a norm on `X`, agrees with the given norm on `Y`, and satisfies `K^-1 * ||x|| <= ||x||_2 <= K * ||x||`, and its `#print axioms` lines report only `propext`, `Classical.choice` and `Quot.sound`, with no `sorryAx`.
:::
