---
title: Common Inequalities
order: 23
---

title: Basics

# Common Inequalities

## The GOATs

[[PR-X5D4Z]]

[[FF-4XBYG]]

:::{.remark title="Different forms of CS"}
In general, Cauchy-Schwarz relates inner product to norm, and only happens to relate norms in $L^1$.
Some other useful forms:
\[
\left(\sum_{k=1}^{n} a_{k} b_{k}\right)^{2} 
&\leq\left(\sum_{k=1}^{n} a_{k}^{2}\right)\left(\sum_{k=1}^{n} b_{k}^{2}\right) \\
\left|\int_{\mathbb{R}^{n}} f(x) \overline{g(x)} d x\right|^{2} 
&\leq \int_{\mathbb{R}^{n}}|f(x)|^{2} d x \int_{\mathbb{R}^{n}}|g(x)|^{2} d x
.\]

:::

[[PR-IJOPU]]

[[FF-2M3OC]] [[FF-3AABE]]

[[PR-7BGSE]]

[[FF-OQ6YZ]]

:::{.proof title="of Holder's inequality"}
It suffices to show this when $\norm{f}_p = \norm{g}_q = 1$, since
\[  
\|f g\|_{1} \leq\|f\|_{p}\|f\|_{q} \Longleftrightarrow \int \frac{|f|}{\|f\|_{p}} \frac{|g|}{\|g\|_{q}} \leq 1
.\]

Using $AB \leq \frac 1 p A^p + \frac 1 q B^q$, we have
\[  
\int|f \| g| \leq \int \frac{|f|^{p}}{p} \frac{|g|^{q}}{q}=\frac{1}{p}+\frac{1}{q}=1
.\]

:::

:::{.example title="Application of Holder's inequality: containment of $L^p$ spaces"}
For finite measure spaces,
\[
1 \leq p < q \leq \infty \implies L^q \subset L^p \quad (\text{ and } \ell^p \subset \ell^q)
.\]

:::

:::{.proof title="of containment of $L^p$ spaces"}
Fix $p, q$, let $r = \frac q p$ and $s = \frac{r}{r-1}$ so $r\inv + s\inv = 1$.
Then let $h = \abs{f}^p$:

\[  
\pnorm{f}{p}^p 
= \pnorm{h\cdot 1}1 \leq \pnorm{1}s \pnorm{h}r 
= \mu(X)^{\frac 1 s} \pnorm{f}q^{\frac q r}
\implies \pnorm{f}p 
\leq \mu(X)^{\frac 1 p - \frac 1 q} \pnorm{f}q
.\]

> Note: doesn't work for $\ell_p$ spaces, but just note that $\sum \abs{x_n} < \infty \implies x_n < 1$ for large enough $n$, and thus $p<q \implies \abs{x_n}^q \leq \abs{x_n}^q$.

:::

[[PR-RYVI7]]

[[PR-ZI7M3]]

:::{.remark}
This appears in several other forms:
\[
{1\over 2\pi} \int_{(-\pi, \pi)} \abs{f}^2 = \sum_{k\in \ZZ} \abs{c_k}^2 && c_k \da {1\over 2\pi } \int_{(-\pi, \pi)} f(x) e^{-ikx} \dx
.\]

:::

[[PR-CCDRN]]

[[PR-JCZKL]]

## Less common

[[PR-YO7MV]]

[[FD-3BK6U]]

[[PR-XUVZY]]

[[FT-ST72T]] [[FF-CKSA3]]

:::{.remark}
This does not handle $p=\infty$ case.
Use to prove $L^p$ is a normed space.

:::

:::{.proof title="of Minkowski's inequality"}
\envlist

- We first note
\[  
\abs{f+g}^p = \abs{f+g}\abs{f+g}^{p-1} \leq \left( \abs{f} + \abs{g}\right) \abs{f+g}^{p-1}
.\]

- Note that if $p,q$ are conjugate exponents then
\[  
\frac 1 q &= 1 - \frac 1 p = \frac{p-1} p \\
q &= \frac p {p-1} 
.\]

- Then taking integrals yields
\[  
\norm{f+g}_p^p &=
\int \abs{f+g}^p \\
&\leq \int \left( \abs{f} + \abs{g}\right) \abs{f+g}^{p-1} \\ 
&= \int \abs{f} \abs{f+g}^{p-1} + \int \abs{g} \abs{f+g}^{p-1} \\
&= \norm{f(f+g)^{p-1}}_1 + \norm{g(f+g)^{p-1}}_1 \\
&\leq \norm{f}_p ~\norm{(f+g)^{p-1})}_q + \norm{g}_p ~\norm{(f+g)^{p-1})}_q \\
&= \left( \norm{f}_p + \norm{g}_p \right) \norm{ (f+g)^{p-1})}_q \\
&= \left( \norm{f}_p + \norm{g}_p \right) \left( \int \abs{f+g}^{(p-1)q} \right)^{\frac 1 q} \\
&= \left( \norm{f}_p + \norm{g}_p \right) \left( \int \abs{f+g}^{p} \right)^{1 - \frac 1 p} \\
&= \left( \norm{f}_p + \norm{g}_p \right) \frac{\int \abs{f+g}^{p} }{\left( \int \abs{f+g}^{p} \right)^{\frac 1 p}} \\
&= \left( \norm{f}_p + \norm{g}_p \right)  \frac{\norm{f+g}_p^p}{\norm{f+g}_p}
.\]

- Cancelling common terms yields
\[  
1 &\leq \left( \norm{f}_p + \norm{g}_p \right) \frac{1}{\norm{f+g}_p} \\
&\implies 
\norm{f+g}_p
\leq \norm{f}_p + \norm{g}_p 
.\]

:::
  
[[PR-2P7FZ]]

[[FF-AVCZA]] [[FF-WV2QN]]

:::{.remark title="some useful special cases"}
\[  
\norm{f\ast g}_1      & \leq \norm{f}_1 \norm{g}_1 \\
\|f * g\|_{p}         & \leq \norm{f}_1 \norm{g}p, \\
\norm{f\ast g}_\infty & \leq \norm{f}_2 \norm{g}_2 \\
\norm{f\ast g}_\infty & \leq \norm{f}_p \norm{g}_q
.\]

:::

## Inequalities that appear in proofs 

[[PR-IQYTA]]

[[PR-W4ICW]]

[[PR-BPOH2]]

[[PR-7KTA6]]

[[PR-OPSAC]]

[[FF-Z3E3C]]

[[PR-CHY3F]]

:::{.proof}
\envlist

- It's an equality when $t=0$.
- $\dd{}{t} 1+ t < \dd{}{t}e^t \iff t<0$

:::

[[PR-2C3SZ]]

- $\sqrt{x + y} \leq \sqrt{x} + \sqrt{y}$.
