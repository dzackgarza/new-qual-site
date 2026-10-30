---
schema: qual/card@1
id: P-LIA5G
kind: problem
title: Maximum modulus principle and zeros when $\abs{f}$ is constant on $\partial U$
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Open Mapping Theorem
  - Zeros
relations: []
review: draft
---

::: {.problem}
Suppose that $U$ is a bounded, open and simply connected domain in $\CC$ and that $f(z)$ is a complex-valued non-constant continuous function on $\bar{U}$ whose restriction to $U$ is holomorphic.

- Prove the maximum modulus principle by showing that if $z_{0} \in U$, then

$$
\abs{f\left(z_{0}\right)}<\sup \{\abs{f(z)}: z \in \partial U\} .
$$

- Show furthermore that if $\abs{f(z)}$ is constant on $\partial U$, then $f(z)$ has a zero in $U$ (i.e., there exists $z_{0} \in U$ for which $f\left(z_{0}\right)=0$ ).
:::

::: {.solution}

::: pf

::: {.pf-step #nonconst}

$f$ is nonconstant on $U$.

::: pf-proof

If $f$ were constant on $U$, it would be constant on $\overline U$ by continuity, because $U$ is dense in $\overline U$.

:::

:::

::: {.pf-step #maxmod}

For every $z_0\in U$, $\abs{f(z_0)}<\sup\{\abs{f(z)}:z\in\partial U\}$.

::: pf-proof

The set $\overline U$ is compact, so $\abs{f}$ attains a maximum $M$ on $\overline U$. By Step [](#nonconst){.pf-ref} and the open mapping theorem on the domain $U$, $f(U)$ is open. For $z_1\in U$, $f(U)$ contains a disk about $f(z_1)$, and that disk contains a point of modulus greater than $\abs{f(z_1)}$. So $\abs{f(z_1)}<M$ for every $z_1\in U$, and the maximum $M$ is attained at a point of $\partial U$. Hence $\abs{f(z_0)}<M=\max_{\partial U}\abs{f}$.

:::

:::

::: {.pf-step #zero}

If $\abs{f}=C$ on $\partial U$, then $f$ has a zero in $U$.

::: pf-proof

By Step [](#maxmod){.pf-ref}, $0\le\abs{f(z_0)}<C$ for $z_0\in U$, so $C>0$. Suppose $f$ has no zero in $U$. Then $f$ has no zero on $\overline U$, so $1/f$ is continuous on $\overline U$, holomorphic and nonconstant on $U$, with $\abs{1/f}=1/C$ on $\partial U$. Step [](#maxmod){.pf-ref} applied to $1/f$ gives $1/\abs{f(z_0)}<1/C$, that is, $\abs{f(z_0)}>C$, contrary to Step [](#maxmod){.pf-ref} applied to $f$.

:::

:::

::: pf-qed

Steps [](#maxmod){.pf-ref} and [](#zero){.pf-ref} prove the two parts.

:::

:::

:::
