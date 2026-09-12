---
schema: qual/card@1
id: P-ALGS09F
kind: problem
title: "Classification of finitely generated modules over a local PID"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 6 of the official UCSD Spring 2009 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Classified finitely generated modules using the unique irreducible class of a local PID and constructed an explicit nonzero map between cyclic torsion summands.
---

::: problem
A commutative ring $R$ with identity is local if it has exactly one maximal ideal.
Let $R$ be a local ring which is a PID, but is not a field.

(a) Classify the possible finitely generated $R$-modules, in terms of their invariant factors (or elementary divisors).
Show that there is only a countably infinite number of finitely generated $R$-modules, up to isomorphism.

(b) Prove that if $M$ and $N$ are nonzero, finitely generated, torsion $R$-modules, then there exists a nonzero $R$-module homomorphism $\phi: M \to N$.
:::

::: {.solution}
Let $\mathfrak m$ be the unique maximal ideal of $R$.
Since $R$ is a PID and is not a field,
\[
\mathfrak m=(\pi)
\]
for some nonzero nonunit $\pi\in R$.

<1>1. Every irreducible element of $R$ is associate to $\pi$.
::: {.proof}
Let $q\in R$ be irreducible.
Then $(q)$ is a nonzero prime ideal of the PID $R$, hence a maximal ideal.
Since $R$ has only one maximal ideal,
\[
(q)=\mathfrak m=(\pi).
\]
Thus $q$ and $\pi$ are associates.
:::

<1>2. Every finitely generated $R$-module is isomorphic to
\[
R^r\oplus \bigoplus_{i=1}^t R/(\pi^{e_i})
\]
for integers $r,t\ge0$ and positive integers $e_i$; after reordering one may assume
\[
1\le e_1\le e_2\le\cdots\le e_t.
\]
::: {.proof}
The structure theorem for finitely generated modules over a PID gives
\[
M\cong R^r\oplus\bigoplus_j R/(d_j),
\]
where the nonzero nonunits $d_j$ may be chosen in invariant-factor form, or equivalently decomposed into powers of irreducibles in elementary-divisor form.
By <1>1, every irreducible of $R$ is associate to $\pi$.
Hence every elementary divisor is associate to a power $\pi^e$, giving the displayed decomposition.
Conversely every such finite direct sum is a finitely generated $R$-module.
:::

<1>3. There are only countably infinitely many isomorphism classes of finitely generated $R$-modules.
::: {.proof}
By <1>2, an isomorphism class is determined by a nonnegative integer $r$ and a finite nondecreasing sequence
\[
(e_1,\ldots,e_t)
\]
of positive integers.
The set of all finite sequences of integers is countable, so there are at most countably many isomorphism classes.
There are infinitely many, since
\[
R/(\pi),\ R/(\pi^2),\ R/(\pi^3),\ldots
\]
are pairwise nonisomorphic: the annihilator of $R/(\pi^n)$ is $(\pi^n)$, and these ideals are distinct.
Thus there are exactly countably infinitely many isomorphism classes.
:::

<1>4. For all integers $a,b\ge1$, there is a nonzero homomorphism
\[
R/(\pi^a)\longrightarrow R/(\pi^b).
\]
::: {.proof}
If $a\ge b$, define
\[
\varphi(\overline r)=\overline r.
\]
This is well-defined because
\[
(\pi^a)\subseteq(\pi^b),
\]
and it is nonzero.

If $a<b$, define
\[
\varphi(\overline r)=\overline{r\pi^{b-a}}.
\]
If $r-r'\in(\pi^a)$, then
\[
(r-r')\pi^{b-a}\in(\pi^b),
\]
so the map is well-defined.
It is nonzero because
\[
\pi^{b-a}\notin(\pi^b).
\]
:::

<1>5. If $M$ and $N$ are nonzero finitely generated torsion $R$-modules, then there is a nonzero homomorphism $M\to N$.
::: {.proof}
By <1>2, choose cyclic direct summands
\[
R/(\pi^a)\subseteq M,
\qquad
R/(\pi^b)\subseteq N
\]
with $a,b\ge1$.
Let
\[
p:M\twoheadrightarrow R/(\pi^a)
\]
be the projection onto the chosen summand and
\[
i:R/(\pi^b)\hookrightarrow N
\]
the inclusion of the chosen summand.
By <1>4 there is a nonzero map
\[
\varphi:R/(\pi^a)\to R/(\pi^b).
\]
Then
\[
i\circ\varphi\circ p:M\to N
\]
is nonzero: choose $x$ in the selected summand of $M$ with $\varphi(x)\ne0$.
Thus the required homomorphism exists.
:::
:::
