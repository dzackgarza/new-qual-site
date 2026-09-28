---
schema: qual/card@1
id: P-ALGQUAL18W-I4
kind: problem
title: Semisimplicity over $\mathbb C[x,y]$ versus the coordinate subalgebras
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, Problem 4 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Independently proved both directions for arbitrary modules. The converse
    groups the semisimple C[x]-decomposition into x-eigenspaces, observes that
    these are C[y]-submodules, and decomposes them into one-dimensional
    C[y]-simple modules. This agrees with the recorded source solution.
---

::: {.problem}
True or false?
Justify your answer with a proof or counterexample: a $\mathbb C[x,y]$-module is semisimple if and only if its restrictions to both subalgebras $\mathbb C[x]$ and $\mathbb C[y]$ are semisimple.
:::

::: {.solution}
The statement is **true**. Put
$$
R=\CC[x,y].
$$

<1>1. Every simple $R$-module is one-dimensional over $\CC$.

::: {.proof}
Because $R$ is commutative, every simple $R$-module is of the form
$$
R/\mathfrak m
$$
for a maximal ideal $\mathfrak m\subseteq R$. By the weak Nullstellensatz,
$$
\mathfrak m=(x-a,y-b)
$$
for some
$$
a,b\in\CC.
$$
Hence
$$
R/\mathfrak m
\cong
\CC,
$$
so its complex dimension is one.
:::

<1>2. If an $R$-module $M$ is semisimple, then its restrictions to
$\CC[x]$ and $\CC[y]$ are semisimple.

::: {.proof}
Write
$$
M=\bigoplus_{\lambda\in\Lambda} S_\lambda
$$
with each $S_\lambda$ a simple $R$-module. By step <1>1, every
$S_\lambda$ is one-dimensional over $\CC$; on it,
$$
x
$$
and
$$
y
$$
act by scalars, say $a_\lambda$ and $b_\lambda$.

As a $\CC[x]$-module,
$$
S_\lambda
\cong
\CC[x]/(x-a_\lambda),
$$
which is simple. Thus the same direct sum expresses the restriction of $M$
to $\CC[x]$ as a direct sum of simple modules. Hence that restriction is
semisimple.

The identical argument with $y$ shows that the restriction to $\CC[y]$ is
semisimple.
:::

<1>3. Assume conversely that $M$ is semisimple as a $\CC[x]$-module. Then
$$
\boxed{
M
=
\bigoplus_{a\in\CC} M_a,
\qquad
M_a
=
\{m\in M:xm=am\}.
}
$$

::: {.proof}
Every simple $\CC[x]$-module is
$$
\CC[x]/(x-a)
$$
for some $a\in\CC$, because $\CC$ is algebraically closed. Since $M$ is
semisimple over $\CC[x]$, it is a direct sum of such simple modules.

Group together all simple summands on which $x$ acts by the same scalar
$a$. Their direct sum is exactly the eigenspace
$$
M_a=\{m:xm=am\}.
$$
Summands with different eigenvalues have zero intersection, so the resulting
sum over $a$ is direct.
:::

<1>4. Every $M_a$ is a $\CC[y]$-submodule of $M$.

::: {.proof}
Let
$$
m\in M_a.
$$
Since the actions of $x$ and $y$ commute,
$$
x(ym)
=
y(xm)
=
y(am)
=
a(ym).
$$
Thus
$$
ym\in M_a.
$$
The space $M_a$ is already a complex vector subspace, so it is stable under
all polynomials in $y$. Hence it is a $\CC[y]$-submodule.
:::

<1>5. If the restriction of $M$ to $\CC[y]$ is semisimple, then every
$M_a$ is a semisimple $\CC[y]$-module.

::: {.proof}
A standard characterization of semisimple modules is that every submodule is
a direct summand; equivalently, every submodule of a semisimple module is
semisimple.

By step <1>4,
$$
M_a\subseteq M
$$
is a $\CC[y]$-submodule. Since the restriction of $M$ to $\CC[y]$ is
semisimple by hypothesis, it follows that $M_a$ is semisimple over
$\CC[y]$.
:::

<1>6. Each $M_a$ is a direct sum of one-dimensional $R$-submodules.

::: {.proof}
By step <1>5, decompose
$$
M_a
=
\bigoplus_{\mu\in\Lambda_a} L_\mu
$$
into simple $\CC[y]$-modules. Since $\CC$ is algebraically closed, each
$L_\mu$ is
$$
\CC[y]/(y-b_\mu)
$$
for some $b_\mu\in\CC$, hence is one-dimensional over $\CC$.

On all of $M_a$, the element $x$ acts as the scalar $a$. Therefore every
$L_\mu$ is stable not only under $y$ but also under $x$. Hence it is an
$R=\CC[x,y]$-submodule.

On $L_\mu$, the ring $R$ acts through
$$
R
\longrightarrow
\CC,
\qquad
p(x,y)
\longmapsto
p(a,b_\mu).
$$
Thus $L_\mu$ is a one-dimensional simple $R$-module.
:::

<1>7. If the restrictions of $M$ to both $\CC[x]$ and $\CC[y]$ are
semisimple, then $M$ is semisimple as an $R$-module.

::: {.proof}
Step <1>3 gives
$$
M=\bigoplus_{a\in\CC}M_a.
$$
Step <1>6 decomposes each $M_a$ as a direct sum of simple $R$-modules.
Substituting these decompositions gives
$$
M
=
\bigoplus_{a\in\CC}
\bigoplus_{\mu\in\Lambda_a}
L_\mu,
$$
a direct sum of simple $R$-modules. Hence $M$ is semisimple.
:::

<1>8. Therefore
$$
\boxed{
M\text{ is semisimple over }\CC[x,y]
\iff
M|_{\CC[x]}\text{ and }M|_{\CC[y]}\text{ are semisimple}.
}
$$

::: {.proof}
Step <1>2 proves the forward implication. Step <1>7 proves the converse.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 proves that the statement in the problem is true.
:::
:::
