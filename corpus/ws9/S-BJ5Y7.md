---
schema: qual/card@1
id: S-BJ5Y7
kind: solution
title: Solution to P-S4PJP
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - lp-spaces
  - norms
relations:
- kind: solves
  target: P-S4PJP
review: draft
---

:::{.solution}
(a) Define $\alpha$ to be the number $\ge1$ so that $1/\alpha = 1/q-1/p+1$ (if $q=\infty$ and $p=1$ then $\alpha=\infty$). Then $1/q+1 = 1/p+1/\alpha$, so by Young's convolution inequality we have
$$||f*\phi||_{L^q} \le ||f||_{L^p}||\phi||_{L^\alpha} \le \sup_{x\in\mathbb{R}} |\phi(x)| \cdot ||f||_{L^p}$$
as desired. Now we prove Young's convolution inequality: the statement is that if $1/p+1/q=1/r+1$, and $f\in L^p$ and $g\in L^q$, then $||f*g||_{L^r} \le ||f||_{L^p}||g||_{L^q}$. Proof: note that the condition on $p,q,r$ implies that $1/p,1/q \ge 1/r$. We have
$$1 = \frac{1}{p}+\frac{1}{q}-\frac{1}{r} = \left(\frac1p-\frac1r\right)+\left(\frac1q-\frac1r\right)+\frac1r = \frac{r-p}{pr}+\frac{r-q}{qr}+\frac1r.$$
By Hölder using the three conjugate exponents above, we have
$$|(f*g)(x)| \le \int |f(x-y)g(y)|\,dy$$
$$\le \int |f(x-y)|^{(r-p)/r}|g(y)|^{(r-q)/r}|f(x-y)^{p/r}g(y)^{q/r}|\,dy$$
$$\le \left(\int |f(x-y)|^p\,dy\right)^{(r-p)/pr}\left(\int|g(y)|^q\,dy\right)^{(r-q)/qr}\left(\int |f(x-y)^p g(y)^q|\,dy\right)^{1/r}$$
$$= ||f||_{L^p}^{(r-p)/r}||g||_{L^q}^{(r-q)/r}\left(\int |f(x-y)^p g(y)^q|\,dy\right)^{1/r}.$$
Thus
$$||f*g||_{L^r}^r = \int |(f*g)(x)|^r\,dx \le ||f||_{L^p}^{r-p}||g||_{L^q}^{r-q}\int\int |f(x-y)^p g(y)^q|\,dy\,dx$$
$$= ||f||_{L^p}^{r-p}||g||_{L^q}^{r-q} \int\int |f(x-y)^p g(y)^q|\,dx\,dy \quad \text{by Tonelli}$$
$$= ||f||_{L^p}^r ||g||_{L^q}^r. \quad \square$$

(b) Fix $p>q$. Let $\phi$ be equal to 1 on $[0,1]$, have support contained in $[-1,2]$, and have $0\le\phi\le1$ everywhere. Fix $1/\alpha\in(q,p)$ and let $f(y)=1/y^\alpha$ for $y\in[10,\infty)$ and 0 otherwise. Note that $f\in L^p$ but $f\notin L^q$. We have, for all $x>100$,
$$(f*\phi)(x) = \int f(x-y)\phi(y)\,dy \ge \int_0^1 f(x-y)\,dy = \int_{x-1}^x f(y)\,dy = \int_{x-1}^x \frac{1}{y^\alpha}\,dy \ge \frac{1}{x^\alpha}.$$
Thus $f*\phi \notin L^q$, so the inequality fails. $\square$
:::
