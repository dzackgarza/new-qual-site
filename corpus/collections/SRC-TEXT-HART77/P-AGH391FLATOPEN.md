---
schema: qual/card@1
id: P-AGH391FLATOPEN
kind: problem
title: Flat morphisms of finite type are open
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Constructible Sets
  - Noetherian Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise III.9.1 and its cited Exercises II.3.18--II.3.19 in Hartshorne. The proof uses Chevalley's constructibility theorem and proves generization stability directly from the faithfully flat local map on local rings.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Show that a flat morphism $f: X \to Y$ of finite type of noetherian schemes is open: for every open subset $U \subseteq X$, the image $f(U)$ is open in $Y$.

Hint: show that $f(U)$ is constructible and stable under generization, using (II, Ex.
3.18) and (II, Ex.
3.19).
:::

::: {.solution}
Fix an open subset $U\subseteq X$.

::: pf

::: {.pf-step #s1}

The subset $f(U)\subseteq Y$ is constructible.

::: pf-proof

The open subscheme $U$ is noetherian because $X$ is noetherian, and the restricted morphism
$$
f|_U:U\longrightarrow Y
$$
is of finite type because finite type is preserved by restriction to an open subscheme.
The whole space $U$ is a constructible subset of itself.
Chevalley's theorem, Hartshorne II, Exercise 3.19, says that the image of a constructible subset under a finite-type morphism of noetherian schemes is constructible.
Therefore
$$
f(U)=(f|_U)(U)
$$
is constructible in $Y$.

:::

:::

::: {.pf-step #s2}

A flat local homomorphism of local rings is faithfully flat.

::: pf-proof

Let
$$
(A,\mathfrak m)\longrightarrow(B,\mathfrak n)
$$
be local and flat.
For an $A$-module $M$, suppose
$$
M\otimes_A B=0.
$$
If $M\ne0$, choose $0\ne u\in M$.
Its cyclic submodule is
$$
Au\cong A/I
$$
for a proper ideal $I\subseteq A$, and because $A$ is local we have $I\subseteq\mathfrak m$.
Flatness preserves the injection $Au\hookrightarrow M$, so
$$
(A/I)\otimes_A B\hookrightarrow M\otimes_A B.
$$
But
$$
(A/I)\otimes_A B\cong B/IB.
$$
Because the homomorphism is local,
$$
IB\subseteq\mathfrak mB\subseteq\mathfrak n,
$$
so $B/IB\ne0$, contradicting $M\otimes_A B=0$.
Thus tensoring with $B$ detects the zero module, and a flat module with this property is faithfully flat.

:::

:::

::: {.pf-step #s3}

If $x\in X$, $y=f(x)$, and $y'$ is a generization of $y$, then there is a generization $x'$ of $x$ with
$$
f(x')=y'.
$$

::: pf-proof

The morphism on local rings
$$
\OO_{Y,y}\longrightarrow\OO_{X,x}
$$
is flat because $f$ is flat, and it is a local homomorphism.
By step [](#s2){.pf-ref} it is faithfully flat.
Hence the induced map on spectra
$$
\Spec\OO_{X,x}\longrightarrow\Spec\OO_{Y,y}
$$
is surjective.
Indeed, for any prime $\mathfrak p\subseteq\OO_{Y,y}$, faithful flatness gives
$$
\kappa(\mathfrak p)\otimes_{\OO_{Y,y}}\OO_{X,x}\ne0.
$$
Any nonzero ring has a prime ideal, and a prime of this fibre corresponds to a prime of $\OO_{X,x}$ contracting to $\mathfrak p$.

Points of $\Spec\OO_{Y,y}$ correspond exactly to generizations of $y$ in $Y$, while points of $\Spec\OO_{X,x}$ correspond to generizations of $x$ in $X$.
The point $y'$ therefore has a preimage $x'$ in $\Spec\OO_{X,x}$, and this $x'$ is a generization of $x$ satisfying $f(x')=y'$.

:::

:::

::: {.pf-step #s4}

The constructible subset $f(U)$ is stable under generization.

::: pf-proof

Let $y\in f(U)$ and let $y'$ be a generization of $y$.
Choose $x\in U$ with $f(x)=y$.
By step [](#s3){.pf-ref} there is a generization $x'$ of $x$ with $f(x')=y'$.

Open subsets are stable under generization, so $x\in U$ implies $x'\in U$.
Therefore
$$
y'=f(x')\in f(U).
$$
Thus $f(U)$ is stable under generization.

:::

:::

::: {.pf-step #s5}

The subset $f(U)$ is open in $Y$.

::: pf-proof

Noetherian schemes are Zariski spaces in the sense used in Hartshorne II.3.
Exercise II.3.18(c) says that a subset of a Zariski space is open if and only if it is constructible and stable under generization.
Step [](#s1){.pf-ref} proves constructibility of $f(U)$, and step [](#s4){.pf-ref} proves generization stability.
Hence
$$
\boxed{f(U)\text{ is open in }Y}.
$$
Since $U\subseteq X$ was arbitrary, $f$ is an open map.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves the required openness for every open subset of $X$.

:::

:::

:::
