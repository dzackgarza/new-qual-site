---
schema: qual/card@1
id: P-UTCT-1-23
kind: problem
title: Homotopy classes of plane fields on the lens space $L(p,q)$
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Exercise 1.23 of the retained George D. Torres notes from Bob Gompf's M392C Contact Topology course, Fall 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the construction of Gamma_tau, Corollary 1.21 and Example 1.22, on which the exercise depends, from pp. 5-6 of Gompf Contact Topology.pdf.
---

::: {.problem}
Let $M$ be a closed, oriented $3$-manifold with a trivialization $\tau$ of $TM$, so that oriented plane fields on $M$ up to homotopy correspond to $[M, S^2]$ and hence to framed cobordism classes of framed links in $M$.
Let $\Gamma_\tau$ be the map taking an oriented plane field $\xi$ to the class in $H_1(M)$ of the corresponding framed link; it is onto, and the Euler class satisfies $\operatorname{PD}(e(\xi)) = 2\Gamma_\tau(\xi)$.
Consequently an oriented plane bundle $\xi$ on $M$ is realized as a plane field if and only if $e(\xi) = 2x$ for some $x \in H_1(M)$.

Example: consider $M = \RP^3$.
We know $H_1(\RP^3) = \ZZ/2\ZZ$.
Note that only $0 \in H_1$ can be represented as $2x$, so every plane field in $\RP^3$ is trivial as a plane bundle.
For fixed choice of $\tau$, however, we get two values of $\Gamma_\tau$ and therefore there are at least two different plane fields that are not homotopic.

Analyze the lens space $L(p,q)$ in the same way.
(Hint: $H_1(L(p,q)) = \ZZ/p\ZZ$.)
:::

::: {.solution}

Let
$$
M=L(p,q).
$$
By the hint,
$$
H_1(M;\ZZ)\cong\ZZ/p.
$$
By Poincaré duality for the closed oriented $3$-manifold $M$,
$$
H^2(M;\ZZ)\cong H_1(M;\ZZ)\cong\ZZ/p.
$$

::: pf

::: {.pf-step #s1-1}

For a fixed trivialization $\tau$ of $TM$, the invariant
$$
\Gamma_\tau
$$
is a surjection
$$
\boxed{
\Gamma_\tau:
\{\text{oriented plane fields on }M\}/\simeq
\twoheadrightarrow
\ZZ/p}.
$$


::: pf-proof

This is the surjectivity statement preceding the exercise, applied to
$$
H_1(M)\cong\ZZ/p.
$$

:::

:::

::: {.pf-step #s1-2}

Consequently, for fixed $\tau$, there are at least $p$ distinct
homotopy classes of oriented plane fields on $M$.


::: pf-proof

Plane fields with different values of $\Gamma_\tau$ cannot be homotopic,
since $\Gamma_\tau$ is a homotopy invariant. Step [](#s1-1){.pf-ref} shows that all
$p$ elements of $\ZZ/p$ occur.

:::

:::

::: {.pf-step #s1-3}

For every oriented plane field $\xi$,
$$
\boxed{
\operatorname{PD}(e(\xi))
=
2\Gamma_\tau(\xi)}
$$
in
$$
H_1(M)\cong\ZZ/p.
$$


::: pf-proof

This is the identity established immediately before Corollary 1.21 in the
source notes.

:::

:::

::: {.pf-step #s1-4}

Therefore an oriented $2$-plane bundle over $M$ with Euler class
$e\in H^2(M)$ is realizable as a plane field exactly when
$$
\boxed{
\operatorname{PD}(e)\in2(\ZZ/p)}.
$$


::: pf-proof

Corollary 1.21 says that an oriented plane bundle is realized as a plane
field if and only if
$$
e=2x
$$
under the Poincaré-duality identification with $H_1(M)$.

:::

:::

::: {.pf-step #s1-5}

If $p$ is odd, multiplication by $2$,
$$
d_2:\ZZ/p\to\ZZ/p,
\qquad
x\longmapsto2x,
$$
is an isomorphism.


::: pf-proof

Since
$$
\gcd(2,p)=1,
$$
the class of $2$ is invertible modulo $p$.

:::

:::

::: {.pf-step #s1-6}

Hence, if $p$ is odd,
$$
\boxed{
2(\ZZ/p)=\ZZ/p}.
$$


::: pf-proof

This is surjectivity of the isomorphism in step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Therefore every oriented $2$-plane bundle over $L(p,q)$ is
realizable as a plane field when $p$ is odd.


::: pf-proof

Oriented real rank-$2$ bundles are classified by their Euler class in
$$
H^2(M;\ZZ)\cong\ZZ/p.
$$
By step [](#s1-6){.pf-ref}, every Euler class is divisible by $2$, so step [](#s1-4){.pf-ref} applies
to every bundle class.

:::

:::

::: {.pf-step #s1-8}

For $p$ odd, the Euler class determines the value of
$\Gamma_\tau$.


::: pf-proof

From step [](#s1-3){.pf-ref},
$$
2\Gamma_\tau(\xi)
=
\operatorname{PD}(e(\xi)).
$$
Since multiplication by $2$ is injective by step [](#s1-5){.pf-ref}, the right-hand side
determines the unique value of $\Gamma_\tau(\xi)$.

:::

:::

::: {.pf-step #s1-9}

Thus, for $p$ odd, the $p$ values of $\Gamma_\tau$ obtained in
step [](#s1-1){.pf-ref} give $p$ plane fields whose underlying plane bundles have $p$
different Euler classes.


::: pf-proof

Step [](#s1-8){.pf-ref} says distinct $\Gamma_\tau$-values have distinct doubles, hence
distinct Euler classes. There are $p$ values by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

The kernel of multiplication by $2$ on $\ZZ/p$ is
$$
\boxed{
\ker d_2
=
\{0,r\}}.
$$


::: pf-proof

The congruence
$$
2x\equiv0\pmod{2r}
$$
is equivalent to
$$
x\equiv0\pmod r.
$$
Modulo $2r$, the two such classes are $0$ and $r$.

:::

:::

::: {.pf-step #s1-11}

The image of multiplication by $2$ is
$$
\boxed{
2(\ZZ/p)
=
\{0,2,4,\dots,2r-2\}}
$$
and has order
$$
\boxed{r=p/2}.
$$


::: pf-proof

The image consists of the even residue classes modulo $2r$. By the
first-isomorphism theorem,
$$
\cardinality{\operatorname{im}d_2}
=
\frac{\cardinality{\ZZ/p}}{\cardinality{\ker d_2}}
=
\frac{p}{2}
=
r.
$$

:::

:::

::: {.pf-step #s1-12}

Therefore, when $p$ is even, exactly
$$
\boxed{p/2}
$$
Euler classes occur among plane fields.


::: pf-proof

By step [](#s1-4){.pf-ref}, the realizable Euler classes are exactly the image of
multiplication by $2$. Step [](#s1-11){.pf-ref} gives its cardinality.

:::

:::

::: {.pf-step #s1-13}

Each realizable Euler class has exactly two possible
$\Gamma_\tau$-values.


::: pf-proof

If
$$
2x=2y
$$
in $\ZZ/p$, then
$$
x-y\in\ker d_2
=
\{0,p/2\}
$$
by step [](#s1-10){.pf-ref}. Thus the two solutions differ by $p/2$, and there are
exactly two of them.

:::

:::

::: {.pf-step #s1-14}

Hence, when $p$ is even, there are pairs of nonhomotopic plane
fields having isomorphic underlying oriented plane bundles.


::: pf-proof

Let $x\in\ZZ/p$. By surjectivity of $\Gamma_\tau$, choose plane
fields
$$
\xi,\xi'
$$
with
$$
\Gamma_\tau(\xi)=x,
\qquad
\Gamma_\tau(\xi')=x+p/2.
$$
They are not homotopic because their $\Gamma_\tau$-values differ. But
step [](#s1-3){.pf-ref} and
$$
2(x+p/2)
=
2x+p
=
2x
$$
in $\ZZ/p$ show that
$$
e(\xi)=e(\xi').
$$
Oriented $2$-plane bundles are classified by Euler class, so the underlying
plane bundles are isomorphic.

:::

:::

::: {.pf-step #s1-15}

For $p=2$, this recovers the $\RP^3$ example:
every plane field has trivial Euler class, but $\Gamma_\tau$ takes two
values.


::: pf-proof

When
$$
p=2,
$$
the image of doubling is
$$
\{0\},
$$
while
$$
H_1\cong\ZZ/2
$$
has two elements. This is exactly Example 1.22.

:::

:::

::: pf-step

Summarizing:
$$
\boxed{
\begin{array}{c|c|c}
& \text{realizable Euler classes} &
\Gamma_\tau\text{-values over each Euler class}\\
\hline
p\text{ odd} & p & 1\\
p\text{ even} & p/2 & 2.
\end{array}}
$$


::: pf-proof

For odd $p$, use steps [](#s1-5){.pf-ref} through [](#s1-9){.pf-ref}. For even $p$, use steps
[](#s1-10){.pf-ref} through [](#s1-14){.pf-ref}.

:::

:::

::: pf-step

In either parity, for fixed $\tau$ there are at least $p$
pairwise nonhomotopic plane fields on $L(p,q)$.


::: pf-proof

This is step [](#s1-2){.pf-ref}. The parity analysis describes how those $p$ distinct
$\Gamma_\tau$-values project to Euler classes.

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} through [](#s1-9){.pf-ref} analyze the odd case, and steps [](#s1-12){.pf-ref} through [](#s1-15){.pf-ref} analyze the
even case, including the $\RP^3$ specialization.

:::

:::

:::
