---
schema: qual/card@1
id: P-AGH4420ENDOMORPHISMRINGCHARP
kind: problem
title: The endomorphism ring in characteristic $p$ and the field of definition of $j$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Jacobians
  - Curves
relations: []
review: draft
---

::: problem
Let $X$ be an elliptic curve over a field $k$ of characteristic $p>0$, and let $R=\operatorname{End}(X, P_0)$ be its ring of endomorphisms.

a. Let $X_p$ be the curve over $k$ defined by changing the $k$-structure of $X$ (2.4.1). Show that $j(X_p)=j(X)^{1/p}$. Thus $X \cong X_p$ over $k$ if and only if $j \in \FF_p$.

b. Show that $p_X$ in $R$ factors into a product $\pi \hat{\pi}$ of two elements of degree $p$ if and only if $X \cong X_p$. In this case, the Hasse invariant of $X$ is 0 if and only if $\pi$ and $\hat{\pi}$ are associates in $R$ (i.e., differ by a unit). (Use (2.5).)

c. If $\Hasse(X)=0$ show in any case $j \in \FF_{p^2}$.

d. For any $f \in R$, there is an induced map $f^*: H^1(\OO_X) \to H^1(\OO_X)$. This must be multiplication by an element $\lambda_f \in k$. So we obtain a ring homomorphism $\varphi: R \to k$ by sending $f$ to $\lambda_f$. Show that any $f \in R$ commutes with the (nonlinear) Frobenius morphism $F: X \to X$, and conclude that if $\Hasse(X) \neq 0$, then the image of $\varphi$ is $\FF_p$. Therefore, $R$ contains a prime ideal $\mfp$ with $R/\mfp \cong \FF_p$.
:::
