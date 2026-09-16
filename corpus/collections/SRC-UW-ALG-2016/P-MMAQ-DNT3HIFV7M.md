---
schema: qual/card@1
id: P-MMAQ-DNT3HIFV7M
kind: problem
title: A projective resolution of $k\simeq R/(x,y)$ over $R=k[x,y]$ and $\mathrm{Tor}_i^R((x,y),k)$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homological Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $R = k[x,y]$ where $k$ is a field, and let $I=(x,y)R$.

- Show that `\begin{align*} 0 \to R \mapsvia{\phi} R \oplus R \mapsvia{\psi} R \to k \to 0 \end{align*}`{=tex} where $\phi(a) = (-ya,xa)$, $\psi((a,b)) = xa+yb$ for $a,b \in R$, is a projective resolution of the $R$-module $k \simeq R/I$.

- Show that $I$ is not a flat $R$-module by computing $\Tor_i^R(I,k)$
:::


::: {.solution}
Write \(\varepsilon:R\to k=R/(x,y)\) for the quotient map.

First consider
\[
0\longrightarrow R\xrightarrow{\phi}R^2\xrightarrow{\psi}R\xrightarrow{\varepsilon}k\longrightarrow0,
\]
with
\[
\phi(a)=(-ya,xa),\qquad \psi(a,b)=xa+yb.
\]
All three nonzero modules in the resolution are free, hence projective. We verify exactness.

The map \(\phi\) is injective: if \((-ya,xa)=(0,0)\), then \(xa=0\); since \(R=k[x,y]\) is a domain and \(x\neq0\), we get \(a=0\).

Also \(\psi\phi=0\), because
\[
\psi(-ya,xa)=-xya+yxa=0.
\]
Conversely, suppose \((a,b)\in\ker\psi\). Then
\[
xa=-yb.
\]
Since \(x\) is prime in the UFD \(k[x,y]\) and \(x\nmid y\), we have \(x\mid b\); write \(b=xc\). Substituting gives \(xa=-yxc\), hence \(a=-yc\). Therefore
\[
(a,b)=(-yc,xc)=\phi(c),
\]
so \(\ker\psi=\operatorname{im}\phi\).

Finally,
\[
\operatorname{im}\psi=(x,y)=I=\ker\varepsilon,
\]
and \(\varepsilon\) is surjective. Thus the displayed complex is a projective resolution of \(k\).

For the Tor computation of \(I\), truncate the resolution at \(I=\operatorname{im}\psi\):
\[
0\longrightarrow R\xrightarrow{\phi}R^2\xrightarrow{\psi}I\longrightarrow0.
\]
This is a free resolution of \(I\). Tensoring with \(k=R/I\) gives
\[
0\longrightarrow k\xrightarrow{\phi\otimes 1}k^2\longrightarrow0.
\]
Because \(x\) and \(y\) act as zero on \(k\), the map \(\phi\otimes1\) is the zero map. Hence
\[
\Tor_1^R(I,k)\cong k,
\qquad
\Tor_0^R(I,k)=I\otimes_Rk\cong k^2,
\]
and, since the resolution has length one,
\[
\Tor_i^R(I,k)=0\qquad(i\ge2).
\]
In particular \(\Tor_1^R(I,k)\neq0\). A flat module has vanishing \(\Tor_1\) against every module, so \(I\) is not flat.
:::
