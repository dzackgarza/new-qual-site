---
schema: qual/card@1
id: P-APAS24F
kind: problem
title: Unitary structure and character of $\mathcal{L}(V,W)$ as a $G$-representation
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
---

::: {.problem}
Let $(V,\varphi)$ and $(W,\psi)$ be finite-dimensional unitary representations of a finite group $G$.
Let $\mathcal{L}(V,W)=\{\text{linear }T\colon V\to W\}$ equipped with the scalar product $\langle S,T\rangle=\operatorname{Tr}(S^*T)$.
For $g\in G$ and $T\in\mathcal{L}(V,W)$, put
\[
\omega(g)T=\psi(g)\,T\,\varphi(g^{-1}).
\]
Show that $(\mathcal{L}(V,W),\omega)$ is a unitary representation of $G$.
Compute the character of $(\mathcal{L}(V,W),\omega)$ in terms of the characters of $(V,\varphi)$ and $(W,\psi)$, showing your calculations.
:::

::: {.solution}
First, $\omega$ is a representation. Indeed,
\[
\omega(gh)T
=\psi(gh)T\varphi((gh)^{-1})
=\psi(g)\psi(h)T\varphi(h^{-1})\varphi(g^{-1})
=\omega(g)(\omega(h)T).
\]
Also $\omega(e)=I$.

Now verify unitarity for the Hilbert--Schmidt inner product. Since $\varphi(g)$ and $\psi(g)$ are unitary,
\[
\varphi(g)^{-1}=\varphi(g)^*,
\qquad
\psi(g)^{-1}=\psi(g)^*.
\]
Hence
\[
\begin{aligned}
\langle \omega(g)S,\omega(g)T\rangle
&=\operatorname{Tr}\!\left((\psi(g)S\varphi(g^{-1}))^*\psi(g)T\varphi(g^{-1})\right)\\
&=\operatorname{Tr}\!\left(\varphi(g)S^*\psi(g)^*\psi(g)T\varphi(g^{-1})\right)\\
&=\operatorname{Tr}\!\left(\varphi(g)S^*T\varphi(g)^{-1}\right)\\
&=\operatorname{Tr}(S^*T).
\end{aligned}
\]
Thus $\omega(g)$ is unitary for every $g$.

For the character, use the natural isomorphism
\[
\mathcal L(V,W)\cong W\otimes V^*.
\]
Under this identification, the action is
\[
\psi\otimes\varphi^*.
\]
Therefore
\[
\chi_{\mathcal L(V,W)}(g)
=\chi_W(g)\,\chi_{V^*}(g).
\]
For a unitary representation,
\[
\chi_{V^*}(g)=\chi_V(g^{-1})=\overline{\chi_V(g)}.
\]
Hence
\[
\boxed{\chi_{\omega}(g)=\chi_W(g)\,\overline{\chi_V(g)}.}
\]
:::
