---
schema: qual/card@1
id: S-WCJRK
kind: solution
title: Solution to P-QSYKP
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - PDEs
  - Norms
relations:
- kind: solves
  target: P-QSYKP
review: draft
---

:::{.solution}
A straightforward computation shows that
$$u(x,y) = \sum_{n,m} a_{n,m}(1+4\pi^2(n^2+m^2))e^{2\pi i(nx+my)}.$$
Thus, using orthonormality and the fact that only finitely many coefficients are nonzero, we have
$$\int_0^1\int_0^1 |u(x,y)|^2\,dx\,dy = \int_0^1\int_0^1 \sum_{n,m,k,\ell} a_{n,m}\overline{a_{k,\ell}}(1+4\pi^2(n^2+m^2))(1+4\pi^2(k^2+\ell^2))e^{2\pi i(nx+my)}e^{-2\pi i(kx+\ell y)}\,dx\,dy$$
$$= \sum_{n,m,k,\ell} a_{n,m}\overline{a_{k,\ell}}(1+4\pi^2(n^2+m^2))(1+4\pi^2(k^2+\ell^2))\int_0^1 e^{2\pi i(n-k)x}\,dx\int_0^1 e^{2\pi i(m-\ell)y}\,dy$$
$$= \sum_{n,m} |a_{n,m}|^2(1+4\pi^2(n^2+m^2))^2.$$
Now we simply estimate $v$ using the triangle inequality and Cauchy-Schwarz:
$$|v(x,y)|^2 \le \left(\sum_{n,m}|a_{n,m}|\right)^2 = \left(\sum_{n,m}|a_{n,m}|(1+4\pi^2(n^2+m^2))\cdot \frac{1}{(1+4\pi^2(n^2+m^2))}\right)^2$$
$$\le \left(\sum_{n,m}|a_{n,m}|^2(1+4\pi^2(n^2+m^2))^2\right)\left(\sum_{n,m}\frac{1}{(1+4\pi^2(n^2+m^2))^2}\right)$$
$$= C\cdot ||u||^2_{L^2([0,1]^2)}$$
because $\sum_{n,m}\frac{1}{(1+4\pi^2(n^2+m^2))^2}$ converges. Thus we have established $||v||^2_{L^\infty([0,1]^2)} \le C||u||^2_{L^2([0,1]^2)}$ which implies the desired result. $\square$
:::
