---
schema: qual/card@1
id: P-CAFA19D
kind: problem
title: "Counting roots of z^7 - 2z^5 + b in the unit disk and annulus"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $b \in \mathbb{D}$ and set $f(z) = z^7 - 2z^5 + b$.

(a) How many roots (counting multiplicity) does $f$ have in $\mathbb{D}$?
How many simple roots does $f$ have in $\mathbb{D}$?

(b) How many simple roots does $f$ have in $\{1 \leq |z| < 2\}$?
:::

::: solution
On $|z|=1$,
\[
|z^7+b|\le 1+|b|<2=|-2z^5|.
\]
By Rouché's theorem, $f$ and $-2z^5$ have the same number of zeros in
$\mathbb D$, namely $5$, counted with multiplicity.

We next determine multiplicities. Since
\[
f'(z)=z^4(7z^2-10),
\]
the only critical points are $0$ and $\pm\sqrt{10/7}$. If $b\ne0$, then
$f(0)=b\ne0$. At $z=\pm\sqrt{10/7}$, the condition $f(z)=0$ would force
\[
|b|=\left|z^5(2-z^2)\right|
=\frac47\left(\frac{10}{7}\right)^{5/2}>1,
\]
contrary to $|b|<1$. Thus for $b\ne0$ all five zeros in $\mathbb D$ are
simple. If $b=0$, then
\[
f(z)=z^5(z^2-2),
\]
so the only zero in $\mathbb D$ is $0$, with multiplicity $5$, and hence
there are no simple zeros in $\mathbb D$.

On $|z|=2$,
\[
|-2z^5+b|\le 64+|b|<65<128=|z^7|.
\]
So Rouché gives seven zeros in $|z|<2$, counted with multiplicity. Since five
lie in $|z|<1$, exactly two lie in $1\le |z|<2$. The critical-point argument
above shows that these are simple (also when $b=0$, when they are
$\pm\sqrt2$). Therefore there are exactly two simple zeros in the annulus.
:::
