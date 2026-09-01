---
schema: qual/card@1
id: P-QSYKP
kind: problem
title: $\|v\|_{L^\infty([0,1]^2)}\le C\|v-\Delta v\|_{L^2([0,1]^2)}$ for trigonometric
  polynomials $v$
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - PDEs
  - Norms
relations: []
review: draft
---

::: {.problem}
Let $v$ be a trigonometric polynomial in two variables, i.e. $$v(x,y) = \sum_{n,m\in\mathbb{Z}} a_{n,m} e^{2\pi i(nx+my)}$$ with only finitely many nonzero $a_{n,m}$.
If $u=v-\Delta v$ where $\Delta = \partial_x^2 + \partial_y^2$ is the Laplacian, prove that $$||v||_{L^\infty([0,1]^2)} \le C||u||_{L^2([0,1]^2)}$$ for some constant $C$ independent of $v$.
:::

:::{.solution}
Write $u$ as a Fourier series $u(x,y) = \sum_{n,m} a_{n,m} e^{2\pi i(nx+my)}$.
Applying the Laplacian term by term, each mode $e^{2\pi i(nx+my)}$ is an eigenfunction of $\Delta = \partial_x^2 + \partial_y^2$ with eigenvalue $-4\pi^2(n^2+m^2)$:
\[
\Delta e^{2\pi i(nx+my)} = \left((2\pi i n)^2 + (2\pi i m)^2\right) e^{2\pi i(nx+my)} = -4\pi^2(n^2+m^2) e^{2\pi i(nx+my)}.
\]
Therefore, since $u = v - \Delta v$, the Fourier coefficients of $u$ are $a_{n,m}(1+4\pi^2(n^2+m^2))$:
$$u(x,y) = \sum_{n,m} a_{n,m}(1+4\pi^2(n^2+m^2))e^{2\pi i(nx+my)}.$$
Thus, using orthonormality and the fact that only finitely many coefficients are nonzero, we have
$$\int_0^1\int_0^1 |u(x,y)|^2\,dx\,dy = \int_0^1\int_0^1 \sum_{n,m,k,\ell} a_{n,m}\overline{a_{k,\ell}}(1+4\pi^2(n^2+m^2))(1+4\pi^2(k^2+\ell^2))e^{2\pi i(nx+my)}e^{-2\pi i(kx+\ell y)}\,dx\,dy$$
$$= \sum_{n,m,k,\ell} a_{n,m}\overline{a_{k,\ell}}(1+4\pi^2(n^2+m^2))(1+4\pi^2(k^2+\ell^2))\int_0^1 e^{2\pi i(n-k)x}\,dx\int_0^1 e^{2\pi i(m-\ell)y}\,dy$$
$$= \sum_{n,m} |a_{n,m}|^2(1+4\pi^2(n^2+m^2))^2.$$
Now we estimate $v$ using the triangle inequality and Cauchy-Schwarz:
$$|v(x,y)|^2 \le \left(\sum_{n,m}|a_{n,m}|\right)^2 = \left(\sum_{n,m}|a_{n,m}|(1+4\pi^2(n^2+m^2))\cdot \frac{1}{(1+4\pi^2(n^2+m^2))}\right)^2$$
$$\le \left(\sum_{n,m}|a_{n,m}|^2(1+4\pi^2(n^2+m^2))^2\right)\left(\sum_{n,m}\frac{1}{(1+4\pi^2(n^2+m^2))^2}\right)$$
$$= C\cdot ||u||^2_{L^2([0,1]^2)}$$
because $\sum_{n,m}\frac{1}{(1+4\pi^2(n^2+m^2))^2}$ converges. Thus we have established $||v||^2_{L^\infty([0,1]^2)} \le C||u||^2_{L^2([0,1]^2)}$ which implies the desired result. $\square$
:::
