---
schema: qual/card@1
id: S-2NCCP
kind: solution
title: Solution to P-QZE53
classification:
  areas:
  - real-analysis
  topics: []
relations:
- kind: solves
  target: P-QZE53
review: draft
---

:::{.solution}
(a) The second half of the assertion implies the first half, so we focus on the second. It's enough to show that $\int_{|z|\le R} |F(z)|\,dA(z) < \infty$ for each $R$. We estimate
$$\int_{|z|\le R} |F(z)|\,dA(z) \le \int_{|z|\le R}\int_{w\in\mathbb{C}} \frac{1}{|z-w|}\,d\mu(w)\,dA(z) = \int_{w\in\mathbb{C}}\int_{|z|\le R} \frac{1}{|z-w|}\,dA(z)\,d\mu(w) \quad \text{by Tonelli}$$
$$= \int_{|w|\le 2R}\int_{|z|\le R} \frac{1}{|z-w|}\,dA(z)\,d\mu(w) + \int_{|w|>2R}\int_{|z|\le R}\frac{1}{|z-w|}\,dA(z)\,d\mu(w)$$
$$\le \int_{|w|\le 2R}\int_{|z-w|\le 3R}\frac{1}{|z-w|}\,dA(z)\,d\mu(w) + \int_{|w|>2R}\int_{|z|\le R}\frac{1}{R}\,dA(z)\,d\mu(w)$$
$$\le \int_{|w|\le 2R} C_R\,d\mu(w) + \int_{|w|>2R} \pi R\,d\mu(w) \quad \text{where } C_R \text{ is some constant depending on } R$$
$$< \infty$$
because $\mu$ is a finite measure. $\square$

(b) As in part (a), it's enough to prove the assertion with any compact set $K$ replaced by any interval of the form $[-R,R]$. Fix some $R$ and an integer $m$. Then by part (a) and Tonelli's theorem, we know $\int_m^{m+1}\int_{-R}^R |F(x+iy)|\,dx\,dy < \infty$. This implies that there is a set $Y_{m,R}$ of full measure in $[m,m+1]$ such that $\int_{-R}^R |F(x+iy)|\,dx < \infty$ for each $y\in Y_{m,R}$. By setting $Y_m = \bigcap_{R=1}^\infty Y_{m,R}$, we see that $Y_m$ still has full measure in $[m,m+1]$ and now for any $y\in Y_m$, $\int_{-R}^R |F(x+iy)|\,dx < \infty$ for every $R$. Thus we have shown that almost every horizontal line with $y$-intercept in $[m,m+1]$ satisfies the desired property. Now setting $Y = \bigcup_{m=-\infty}^\infty Y_m$, we see that $Y$ is an almost everywhere subset of $\mathbb{R}$ with the property that $y\in Y$ implies $\int_{-R}^R |F(x+iy)|\,dx < \infty$ for every $R$, which is the desired conclusion. In fact, by examining the proof of part (a) it's clear that we actually proved something a bit stronger, which is that $y\in Y$ implies $\int_K \int_{w\in\mathbb{C}} \frac{1}{|x+iy-w|}\,d\mu(w)\,dx < \infty$ for all compact sets $K$ (we'll need this version in part (c)). $\square$

(c) The same argument as in part (b) shows that the analogous result to part (b) for vertical lines also holds. Let $\mathcal{S}$ be the collection of squares $S$ in $\mathbb{C}$ such that all four sides of $S$ lie on lines for which the conclusion of part (b) holds. It's clear that $\mathcal{S}$ is almost every square in $\mathbb{C}$. Thus for $S\in\mathcal{S}$, we have
$$\int_{\partial S} F(z)\,dz = \int_{\partial S}\int_\mathbb{C} \frac{1}{z-w}\,d\mu(w)\,dz = \int_\mathbb{C}\int_{\partial S} \frac{1}{z-w}\,dz\,d\mu(w)$$
$$= \int_\mathbb{C} 2\pi i\,\chi_S(w)\,d\mu(w) = 2\pi i\,\mu(S),$$
which is the desired result. We just need to justify switching the order of integration in the first line. Note that by definition of $\mathcal{S}$,
$$\int_{\partial S}\int_\mathbb{C} \frac{1}{|z-w|}\,d\mu(w)\,dz$$
is simply a sum of four integrals along horizontal or vertical lines which are known to be finite by the comment at the end of part (b). Thus Fubini-Tonelli applies, so the switch is justified. $\square$
:::
