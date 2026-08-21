---
schema: qual/card@1
id: P-IP7XN
kind: problem
title: $z\sin z=a$ has only real solutions
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Trigonometry
relations: []
review: draft
solved: true
---

:::{.problem title="?"}
Show that $z\sin(z) = a$ has only real solutions.
:::

:::{.solution}
Consider $f(z) \da z\sin(z) - a$.

Big: $M(z) \da z\sin(z)$.
Small: $m(z) \da -a$.

Use the following estimate:

\[
\abs{z\sin(z)}^2
&= \abs{z\over 2}^2 \abs{e^{iz} - e^{-iz}}^2 \\
&\geq \abs{z\over 2}^2 \abs{ \abs e^{iz} } - \abs{ e^{-iz} } ^2 \\
&= \abs{z\over 2}^2 \abs{e^{-\Im(z)} - e^{\Im(z)} } \\
&\convergesto{\Im(z)\to\infty} \infty
,\]
and so in particular a radius $R$ can be chosen large enough so that $\abs{z\sin(z)} > a$ for any $a$.
Thus for $\abs{z} = R$,
\[
\abs{m(z)} = \abs{a} \leq \abs{z\sin(z)} < \abs{M(z)}
\implies \size Z_{M} = \size Z_{M+m} = \size Z_f
.\]
To count the number of zeros of $z\sin(z)$, note that this equals zero at $z=0$ with multiplicity two and $z= k\pi$ for $k\in \ZZ$.
Choosing $R = {\pi \over 2} + n\pi$ for $n$ large enough, there are exactly $2n+2$ such zeros (with multiplicity) to $z\sin(z)$, and thus $2n+2$ zeros to $z\sin(z) - a$.
Now using that $z\sin(z) - a$ has exactly $2n+2$ *real* roots (??), this must be all of them.


> Unsure how to find any roots of this thing, real or not!

:::

