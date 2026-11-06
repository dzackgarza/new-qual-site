---
schema: qual/card@1
id: P-PRACT20-W6-25
kind: problem
title: Injectivity of $g\circ f$ forces injectivity of $f$
classification:
  areas:
  - prelim
  topics:
  - Functions
  - Injectivity
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the arrow lost from g composed with f, checked against Week6_solns.pdf (Problem 25).
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Repaired the garbled quantifier x, y in S in the solution, checked against Week6_solns.pdf (Problem 25).
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against page 11 of the retained solutions booklet GRE Prep:
    Miscellaneous Practice Problem Solutions by Christian Parkinson
    (assets/attachments/prelim-practice-week6-2020/page-11.png), which prints
    this problem with a worked solution. The practice sheet itself is not
    retained and the collection's provenance list is empty, so the statement was
    compared with the card from that page: the printed problem is (a) prove f is one-to-one and (b) show by example that g need not be, which is what the card states
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The printed solution's argument and its example f(x) = e^x, g(x) = x^2 over the reals are transcribed, with the injectivity of the composite checked.
---

::: {.problem}
Let $S, T, U$ be nonempty sets and $f : S \to T$, $g : T \to U$ be functions such that $g \circ f : S \to U$ is one-to-one.

(a) Prove that $f$ is one-to-one.

(b) Show by example that $g$ need not be one-to-one.
:::

::: {.solution}

Let $f\colon S\to T$ and $g\colon T\to U$ with $g\circ f$ one-to-one.

::: pf

::: {.pf-step #injective}

(a) $f$ is one-to-one.

::: pf-proof

If $f(x)=f(y)$ for $x,y\in S$, applying $g$ gives $(g\circ
f)(x)=g(f(x))=g(f(y))=(g\circ f)(y)$, and injectivity of $g\circ f$ gives
$x=y$. So $f$ is injective. This is the contrapositive form of the printed
argument: were $f$ not injective there would be $x\ne y$ with $f(x)=f(y)$ and
hence $(g\circ f)(x)=(g\circ f)(y)$.

:::

:::

::: {.pf-step #notneeded}

(b) $g$ need not be one-to-one: with $S=T=U=\RR$, $f(x)=e^x$ and $g(x)=x^2$,
the composite $x\mapsto e^{2x}$ is one-to-one while $g$ is not.

::: pf-proof

$e^x$ is injective, so $g\circ f$ is injective as the composite of an
injection with the injection $x\mapsto x^2$ restricted to
$e^{\RR}\subseteq(0,\infty)$. But $g(-1)=g(1)=1$ with $-1\ne1$, so $g$ is not
injective. So injectivity of the composite constrains $g$ only on the range of
$f$, which is exactly the content of the printed remark.

:::

:::

:::


:::
