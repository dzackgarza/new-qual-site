---
schema: qual/card@1
id: P-AGH421PNSIMPLYCONNECTED
kind: problem
title: $\PP^n$ is simply connected
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.2.1 together with the IV.2.5.3 computation for P^1.
    The induction step was cross-checked against Hartshorne III.7.9: the inverse
    image of a hyperplane under a connected finite etale cover is the support of
    an ample divisor and is therefore connected.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Use (2.5.3) to show that $\PP^n$ is simply connected.
:::

::: {.solution}
Here **simply connected** means that every finite étale cover is trivial.

::: pf

::: {.pf-step #s1}

It is enough to prove that every connected finite étale cover
$$
f:Y\longrightarrow\PP^n
$$
is an isomorphism.

::: pf-proof

A finite étale cover has only finitely many connected components. The
image of each nonempty connected component is open because an étale
morphism is open, and closed because a finite morphism is closed. Since
$\PP^n$ is connected, each component maps surjectively to $\PP^n$ and is
itself a connected finite étale cover.

Thus, if every connected cover is an isomorphism, an arbitrary finite
étale cover is a finite disjoint union of copies of $\PP^n$, which is
exactly a trivial cover.

:::

:::

::: {.pf-step #s2}

The assertion holds for $n=1$.

::: pf-proof

This is Hartshorne IV.2.5.3: $\PP^1$ has no nontrivial connected finite
étale cover. Equivalently,
[[D-IV2ETCOV|the Riemann--Hurwitz computation for $\PP^1$]]
shows that a connected finite étale cover of $\PP^1$ has degree one and
is an isomorphism.

:::

:::

::: {.pf-step #s3}

Assume $n\ge2$ and that $\PP^{n-1}$ is simply connected. Let
$$
f:Y\longrightarrow\PP^n
$$
be a connected finite étale cover. Then $Y$ is a normal projective
integral variety of dimension $n$.

::: pf-proof

Since $f$ is finite and $\PP^n$ is projective, $Y$ is projective. Since
$f$ is étale and $\PP^n$ is smooth over $k$, the scheme $Y$ is smooth,
hence regular and normal.

A regular scheme has pairwise disjoint irreducible components: at an
intersection point the local ring would have more than one minimal prime,
whereas a regular local ring is a domain. Thus its irreducible components
are open and closed. Because $Y$ is connected, it has only one
irreducible component. Hence $Y$ is integral. Étale morphisms preserve
dimension, so $\dim Y=n$.

:::

:::

::: {.pf-step #s4}

If
$$
H\cong\PP^{n-1}\subseteq\PP^n
$$
is a hyperplane and
$$
D=f^{-1}(H),
$$
then $D$ is connected.

::: pf-proof

The hyperplane $H$ is an effective Cartier divisor with
$$
\mco_{\PP^n}(H)\cong\mco_{\PP^n}(1).
$$
Since $f$ is flat, its pullback
$$
D=f^*H
$$
is an effective Cartier divisor on $Y$, and
$$
\mco_Y(D)
\cong
f^*\mco_{\PP^n}(1).
$$
A finite pullback of an ample invertible sheaf is ample, so
$\mco_Y(D)$ is ample.

By step [](#s3){.pf-ref}, $Y$ is a normal projective variety of dimension at least
two. Hartshorne III.7.9, the Enriques--Severi--Zariski connectedness
theorem, therefore says that the support of the effective ample divisor
$D$ is connected. Thus $D$ is connected.

:::

:::

::: {.pf-step #s5}

The restriction
$$
f|_D:D\longrightarrow H\cong\PP^{n-1}
$$
is an isomorphism.

::: pf-proof

The square
$$
\begin{CD}
D @>>> Y\\
@V{f|_D}VV @VV{f}V\\
H @>>> \PP^n
\end{CD}
$$
is cartesian. Hence $f|_D$ is the base change of the finite étale
morphism $f$, so it is finite étale. Step [](#s4){.pf-ref} says that $D$ is
connected. By the induction hypothesis, every connected finite étale
cover of $\PP^{n-1}$ is an isomorphism. Therefore $f|_D$ is an
isomorphism.

:::

:::

::: {.pf-step #s6}

The morphism $f$ has degree one and is an isomorphism.

::: pf-proof

A finite étale morphism is finite locally free of constant rank on the
connected target $\PP^n$. This rank is its degree and is preserved by
base change. Hence
$$
\deg f
=
\deg(f|_D)
=
1
$$
by step [](#s5){.pf-ref}.

Since $Y$ and $\PP^n$ are integral, $f$ induces an extension of function
fields of degree one, so it is birational. It is also finite, while
$\PP^n$ is normal. A finite birational morphism onto a normal integral
scheme is an isomorphism. Thus $f$ is an isomorphism.

:::

:::

::: {.pf-step #s7}

For every $n\ge1$, $\PP^n$ is simply connected.

::: pf-proof

Step [](#s2){.pf-ref} is the base case. Steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} give the induction step from
$n-1$ to $n$. Step [](#s1){.pf-ref} then upgrades the connected-cover statement to
all finite étale covers.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is exactly the required conclusion.

:::

:::

:::
