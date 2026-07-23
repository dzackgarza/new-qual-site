---
schema: qual/card@1
id: P-NC67O
kind: problem
title: "a. Define what it means for a finite extension of fields $E$ over $F$\u2026"
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
---
a. Define what it means for a finite extension of fields $E$ over $F$ to be a *Galois* extension.

b. Determine the Galois group of $f(x) = x^3 - 7$ over $\QQ$, and justify your answer carefully.

c. Find all subfields of the splitting field of $f(x)$ over $\QQ$.

:::{.solution}
Part a:

- A finite extension $E/F$ is **Galois** if it is normal and separable:
  - Normal: every $f\in F[x]$ either has no roots in $E$ or all roots in $E$.
  - Separable: every element $e\in E$ has a separable minimal polynomial $m(x)$, i.e. $m$ has no repeated roots.

Part b:

- Note $f$ is irreducible by Eisenstein with $p=7$, and since $\QQ$ is perfect, irreducible implies separable.
- Writing $L \da \SF(f)/\QQ$, this is a Galois extension:
  - $L$ is separable: it is a finite extension of a perfect field, which is automatically separable.
  - $L$ is normal: $L$ is the splitting field of a separable polynomial, and thus normal.
- Since $f$ is degree 3, we have $G\da \Gal(L/k) \leq S_3$, and since $G$ is a transitive subgroup the only possibilities are
\[
G = S_3 \cong D_3, A_3 \cong C_3
.\]

- Factor $x^3 - 7 = (x-\omega)(x-\zeta_3\omega)(x-\zeta_3^2\omega)$ where $\omega \da 7^{1\over 3}$ and $\zeta_3$ is a primitive 3rd root of unity.
  Then $L = \QQ(\zeta_3, \omega)$.
  - Aside: label the roots in this order, so $r_1 = \omega, r_2 = \zeta_3\omega, r_3 = \zeta_3^2\omega$.

- Write $\min_{\omega, \QQ}(x) = x^3 - 7$ and let $L_0/\QQ \da \QQ(\omega)/\QQ$ yields $[L_0: \QQ] = 3$.
- Write $\min_{\zeta_3, \QQ}(x) = (x^3-1)/(x-1) = x^2 + x + 1$, and note that this is still the minimal polynomial over $L_0$ since $L_0 \subseteq \RR$ and $\zeta_3 \in \CC\sm\RR$.
  So $[L:L_0] = 2$.

- Counting in towers,
\[
[L:\QQ] = [L:L_0][L_0: \QQ] = (2)(3) = 6
.\]
- But $\# S_3 = 6$ and $\# A_3 = 3$, so $G = S_3$.

- Explicitly, since we can write $\SF(f) = \QQ(\omega, \zeta_3)$, we can find explicit generators:
\[
\sigma:
&\begin{cases}
\omega &\mapsto \omega
\\
\zeta_3 &\mapsto \zeta_3\cdot \zeta_3.
\end{cases}
&&
\implies \sigma \sim (1,2,3) \\
\tau:
&\begin{cases}
\omega &\mapsto \omega
\\
\zeta_3 &\mapsto \bar{\zeta_3}.
\end{cases}
&&
\implies \tau \sim (2, 3)
.\]
  So $G = \gens{\sigma, \tau \st \sigma^3, \tau^2}$.

Part c:

- Note that the subgroup lattice for $S_3$ looks like the following:

![](../../assets/Algebra/UGA%20Questions%20%28no%20solutions%29/sections/figures/2021-08-14_18-00-51.png)

- Note that we can identify
  - $\tau = (2,3)$ which fixes $r_1$
  - $\sigma \tau = (1,2)$ which fixes $r_3$
  - $\sigma^2\tau = (1, 3)$ which fixes $r_2$
  - $\sigma = (1,2,3)$, for which we need to calculate the fixed field.
  Using that $\sigma(\omega) =\zeta\omega$ and $\sigma(\zeta)=\zeta$,
  supposing $\sigma(\alpha) = \alpha$ we have
  \[
  \sigma(\alpha) &\da \sigma(a + b\zeta_3 + c\zeta_3^2 + d\omega + e\zeta_3\omega + f\zeta_3^2\omega) \\
  &= a + b\zeta_3 + c\zeta_3^2 + d\zeta_3\omega + e\zeta_3^2\omega + f\omega \\
  \implies \alpha &= a + b\zeta_3 + c\zeta_3^2 + t_1(\omega + \zeta_3\omega + \zeta_3^2\omega) \\
  \implies \alpha &= a + b\zeta_3 + c\zeta_3^2 + t_1\omega (1 + \zeta_3+ \zeta_3^2) \\
  \implies \alpha &= a + b\zeta_3 + c\zeta_3^2 
  ,\]
  using the general fact that $\sum_{k=0}^{n-1}\zeta_n^k = 0$.
  So the fixed field is $\QQ(1, \zeta, \zeta^2) = \QQ(\zeta)$.

- We thus get the following lattice correspondence:

\begin{tikzcd}
	&& {\QQ(\zeta_3,\omega)} \\
	\\
	{\QQ(\omega) = \QQ(r_1)} & {\QQ(\zeta_3\omega) = \QQ(r_2)} & {\QQ(\zeta_3^2\omega) = \QQ(r_3)} && {\QQ(\zeta_3)} \\
	\\
	&& \QQ \\
	&& 1 \\
	\\
	{\gens{(2,3) = \tau} \cong C_2} & {\gens{(1,3) = \sigma^2\tau} \cong C_2} & {\gens{(1,2) = \sigma\tau} \cong C_2} && {\gens{(1,2,3) = \sigma} \cong C_3} \\
	\\
	&& {\gens{\sigma, \tau}\cong S_3}
	\arrow["3"{description}, from=5-3, to=3-1]
	\arrow["3"{description}, from=5-3, to=3-3]
	\arrow["2"{description}, from=3-1, to=1-3]
	\arrow["2"{description}, from=3-2, to=1-3]
	\arrow["2"{description}, from=3-3, to=1-3]
	\arrow["2"{description}, from=5-3, to=3-5]
	\arrow["3"{description}, from=3-5, to=1-3]
	\arrow["3"{description}, from=5-3, to=3-2]
	\arrow["2"{description}, from=6-3, to=8-1]
	\arrow["3"{description}, from=8-1, to=10-3]
	\arrow["3"{description}, from=8-3, to=10-3]
	\arrow["2"{description}, from=6-3, to=8-3]
	\arrow["3"{description}, from=6-3, to=8-5]
	\arrow["2"{description}, from=8-5, to=10-3]
	\arrow["3"{description}, from=8-2, to=10-3]
	\arrow["2"{description}, from=6-3, to=8-2]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsMTIsWzIsMCwiXFxRUShcXHpldGFfMyxcXG9tZWdhKSJdLFswLDIsIlxcUVEoXFxvbWVnYSkgPSBcXFFRKHJfMSkiXSxbMiwyLCJcXFFRKFxcemV0YV8zXjJcXG9tZWdhKSA9IFxcUVEocl8zKSJdLFsyLDQsIlxcUVEiXSxbMSwyLCJcXFFRKFxcemV0YV8zXFxvbWVnYSkgPSBcXFFRKHJfMikiXSxbNCwyLCJcXFFRKFxcemV0YV8zKSJdLFswLDcsIlxcZ2Vuc3soMiwzKSA9IFxcdGF1fSBcXGNvbmcgQ18yIl0sWzIsOSwiXFxnZW5ze1xcc2lnbWEsIFxcdGF1fVxcY29uZyBTXzMiXSxbMiw1LCIxIl0sWzIsNywiXFxnZW5zeygxLDIpID0gXFxzaWdtYVxcdGF1fSBcXGNvbmcgQ18yIl0sWzQsNywiXFxnZW5zeygxLDIsMykgPSBcXHNpZ21hfSBcXGNvbmcgQ18zIl0sWzEsNywiXFxnZW5zeygxLDMpID0gXFxzaWdtYV4yXFx0YXV9IFxcY29uZyBDXzIiXSxbMywxLCIzIiwxXSxbMywyLCIzIiwxXSxbMSwwLCIyIiwxXSxbNCwwLCIyIiwxXSxbMiwwLCIyIiwxXSxbMyw1LCIyIiwxXSxbNSwwLCIzIiwxXSxbMyw0LCIzIiwxXSxbOCw2LCIyIiwxXSxbNiw3LCIzIiwxXSxbOSw3LCIzIiwxXSxbOCw5LCIyIiwxXSxbOCwxMCwiMyIsMV0sWzEwLDcsIjIiLDFdLFsxMSw3LCIzIiwxXSxbOCwxMSwiMiIsMV1d)

:::
