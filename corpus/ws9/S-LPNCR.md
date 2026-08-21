---
schema: qual/card@1
id: S-LPNCR
kind: solution
title: Solution to P-7Q5AM
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Hilbert Spaces
  - Functional Analysis
relations:
- kind: solves
  target: P-7Q5AM
review: draft
---

:::{.solution}
(a) Fix $x\in B$. We may assume $||x||<1$ because if $x\in S$ the result is obvious. Using a standard Zorn's Lemma/Gram-Schmidt argument, together with the fact that $H$ is infinite-dimensional, we can construct an orthonormal set $\{x/||x||,e_1,e_2,\dots\}$. Let $x_n = x+\sqrt{1-||x||^2}\,e_n$. By the Pythagorean theorem we have $||x_n||^2 = ||x||^2+(1-||x||^2)||e_n||^2 = 1$, so $x_n\in S$. Now we claim that $\{x_n\}$ converges weakly to $x$. For $y\in H$ fixed, we have
$$\langle x_n - x, y\rangle = \sqrt{1-||x||^2}\,\langle e_n,y\rangle.$$
This goes to 0 as $n\to\infty$ because since $\{e_n\}$ is an orthonormal set, Bessel's inequality gives $\sum_{n=1}^\infty |\langle e_n,y\rangle|^2 \le ||y||^2$ and the terms of a convergent series must go to 0. $\square$

(b) Fix an infinite orthonormal set $\{e_1,e_2,\dots\}$. Define $T_n(x):=\langle x,e_n\rangle e_n$. It's clear that $T_n$ is a linear operator $H\to H$. We have $||T_n(x)|| = |\langle x,e_n\rangle|\,||e_n|| \le ||x||$ by Cauchy-Schwarz, so $||T_n||\le 1$. Also it's clear that $T_n(e_n)=e_n$, so $||T_n||=1$. Finally, for any $x\in H$ we have $\lim_{n\to\infty}||T_n(x)|| = \lim_{n\to\infty}|\langle x,e_n\rangle| = 0$ by the same Bessel's inequality argument as in part (a). $\square$
:::
