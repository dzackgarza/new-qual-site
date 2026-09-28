---
order: 220
topics:
- Covering Spaces
- Covering Transformations
- Universal Cover
- Group Actions
- Free Groups
- Free Products
---

# Covering spaces

![A covering map and a lifted path](../../../../assets/assets/Topology/figures/image_2021-01-10-13-45-42.png)

![A more complicated situation](../../../../assets/assets/Topology/figures/image_2021-01-09-00-19-03.png)

## Basic properties

::: {.fact title="Euler characteristics are multiplicative on covering spaces"}
For a finite CW complex $B$ and an $n$-sheeted [[D-ANO2D|covering map]] $p\colon A \to B$ with $n$ finite,
$$
\chi(A) = n\, \chi(B).
$$

:::

::: {.fact}
A covering space of an [[D-K5MLW|orientable]] manifold is an orientable manifold.

:::

::: {.fact}
If $B$ is a manifold with boundary and $p\colon A\to B$ is a covering map, then $A$ is a manifold with boundary and $p^{-1}(\bd B)=\bd A$.

:::

::: {.fact}
For a path-connected covering space $\tilde X$ of a path-connected, locally path-connected space $X$, the deck group acts freely on each fiber, and it acts transitively on each fiber if and only if the cover is [[D-MWD2L|normal]], which holds if and only if $p_*\pi_1(\tilde X,\tilde x_0)$ is a normal subgroup of $\pi_1(X,x_0)$.

:::

## Universal covers

[[D-MWD2L]]

[[PR-UBJ6P]]

::: {.remark}
A Galois cover $\tilde X\to X$ with $\Deck(\tilde X) = G$ is equivalently a principal $G\dash$bundle for a discrete $G$:

\begin{tikzcd}
G 
  \ar[r] 
& 
\tilde X
  \ar[d] 
\\
& 
X 
\end{tikzcd}

:::

[[T-SKJB2]]

[[T-EF5IX]]

::: {.remark title="Lifts from simply connected spaces"}
If $Y$ is simply connected, path-connected, and locally path-connected, then $f_*(\pi_1(Y))$ is trivial, so every map $f\colon Y\to X$ lifts to $\tilde X$.

:::

[[PR-R5EN3]]

[[T-F4PQY]]

::: {.theorem title="Classification of covering spaces"}
Let $X$ be path-connected, locally path-connected, and [[D-EPQ54|semilocally simply connected]], with basepoint $x_0$.
Sending a connected covering space $p\colon(\tilde X,\tilde x_0)\to(X,x_0)$ to $p_*\pi_1(\tilde X,\tilde x_0)$ gives bijections
$$
\begin{aligned}
\correspond{\text{connected based covering spaces } (\tilde X,\tilde x_0)\to(X,x_0)}/\text{based isomorphism}
&\mapstofrom
\correspond{\text{subgroups } H\leq\pi_1(X,x_0)}, \\
\correspond{\text{connected covering spaces } \tilde X\to X}/\text{isomorphism over } X
&\mapstofrom
\correspond{\text{subgroups } H\leq\pi_1(X,x_0)}/\text{conjugacy},
\end{aligned}
$$
under which normal covering spaces correspond to normal subgroups $H\normal\pi_1(X,x_0)$.

:::

[[PR-BHJGY]]

### Examples

::: {.example title="Common covering spaces"}
In each diagram the group on the left is the deck group of the covering map on the right.

\begin{tikzcd}
2\pi \ZZ \cong \ZZ
  \ar[r] 
& 
\hat{S^1} = \RR
  \ar[d, "t\mapsto e^{i t}"] 
\\
& 
S^1 
\end{tikzcd}

Any subgroup $H \leq \pi_1(S^1; 1) = \ZZ$ is of the form $H = n\ZZ$, and the corresponding cover is $\RR/2\pi n\ZZ \cong S^1\to \RR/2\pi\ZZ\cong S^1$, a quotient of the universal cover:

\begin{tikzcd}
	& \ZZ && {\hat{S^1} = \RR} \\
	n\ZZ && {\hat{S^1}/n\ZZ \cong S^1} \\
	&&& {S^1} \\
	&& {S^1}
	\arrow[from=1-2, to=1-4]
	\arrow[from=1-4, to=3-4]
	\arrow[from=2-1, to=2-3]
	\arrow[from=2-3, to=4-3]
	\arrow[dashed, from=2-1, to=1-2]
	\arrow[dashed, from=2-3, to=1-4]
	\arrow[dotted, from=4-3, to=3-4]
\end{tikzcd}

> [Link to Diagram](https://q.uiver.app/?q=WzAsNixbMSwwLCJcXFpaIl0sWzMsMCwiXFxoYXR7U14xfSA9IFxcUlIiXSxbMywyLCJTXjEiXSxbMCwxLCJuXFxaWiJdLFsyLDEsIlxcaGF0e1NeMX0vblxcWlogXFxjb25nIFNeMSJdLFsyLDMsIlNeMSJdLFswLDFdLFsxLDJdLFszLDRdLFs0LDVdLFszLDAsIiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dLFs0LDEsIiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRhc2hlZCJ9fX1dLFs1LDIsIiIsMSx7InN0eWxlIjp7ImJvZHkiOnsibmFtZSI6ImRvdHRlZCJ9fX1dXQ==)

\begin{tikzcd}
\ZZ/n
  \ar[r] 
& 
S^1
  \ar[d, "z\mapsto z^n"] 
\\
& 
S^1 
\end{tikzcd}

\begin{tikzcd}
2\pi i \ZZ \cong \ZZ
  \ar[r] 
& 
\hat{\CC\units} = \CC
  \ar[d, "z\mapsto e^{z}"] 
\\
& 
\CC\units
\end{tikzcd}

\begin{tikzcd}
 \ZZ^{\times n}
  \ar[r] 
& 
\hat{\TT^n} =\RR^n
  \ar[d] 
\\
& 
\TT^n 
\end{tikzcd}

\begin{tikzcd}
\ZZ/2
  \ar[r] 
& 
\hat{\RP^n} = S^n
  \ar[d] 
\\
& 
\RP^n 
\end{tikzcd}

\begin{tikzcd}
\ZZ^{\ast n} 
  \ar[r] 
& 
\widehat{\bigvee^n S^1} = \operatorname{Cayley}(F_n)
  \ar[d] 
\\
& 
\bigvee^n S^1
\end{tikzcd}
where the universal cover is the $2n$-valent Cayley graph of the free group $F_n\cong\ZZ^{\ast n}$ with respect to its free generators.

![For $n=2$](../../../../assets/assets/Topology/figures/2021-07-03_16-55-01.png)

\begin{tikzcd}
\ZZ/n
  \ar[r] 
& 
  \CC\units
  \ar[d, "z\mapsto z^n"] 
\\
& 
\CC\units
\end{tikzcd}

\begin{tikzcd}
\ZZ/p
  \ar[r] 
& 
  S^3
  \ar[d] 
\\
& 
L(p, q)
\end{tikzcd}
where $S^3\subseteq\CC^2$ and the generator of $\ZZ/p$ acts by $(z, w) \mapsto (e^{2\pi i/p} z, e^{2\pi i q/p} w)$ for $q$ coprime to $p$.

The torus double covers the Klein bottle, $T^2 \mapsvia{\times 2} \KK$.

:::

::: {.example title="The circle $S^1$"}
With $S^1 \subseteq \CC$, for $n\geq 1$ the map $p_n\colon S^1 \to S^1$, $z\mapsto z^n$, is an $n$-sheeted covering map.
With $\omega_k(t)\coloneqq e^{2\pi i k t}$, the induced map on fundamental groups is
$$
\begin{aligned}
(p_n)_*\colon \pi_1(S^1) &\to \pi_1(S^1), \\
[\omega_1] &\mapsto [\omega_n] = n[\omega_1],
\end{aligned}
$$
so its image is $n\ZZ$, and the deck group is
$$
\Deck(p_n) \cong \pi_1(S^1)/(p_n)_*\pi_1(S^1) \cong \ZZ/n,
$$
generated by rotation by $2\pi/n$.
The universal cover of $S^1$ is $\RR$, with countably infinite fibers.

:::

::: {.example title="Projective $n\dash$space $\RP^n$"}
For $n\geq 2$, the universal cover of $\RP^n$ is $S^n$, a two-sheeted cover whose fibers are pairs of antipodal points.

:::

::: {.example title="The torus $S^1 \cross S^1$"}
The universal cover of $T = S^1 \cross S^1$ is $\RR \cross \RR\to T$, $(s,t)\mapsto(e^{2\pi i s},e^{2\pi i t})$.
The fiber over the base point is the integer lattice $\ZZ \cross \ZZ$, and $\Deck(\RR^2\to T)\cong\ZZ\cross\ZZ\cong \pi_1(T)$ acts by translations.

:::

[[PR-BXAA5]]

::: {.example title="Wedge of circles"}
The fundamental group of $S^1 \vee S^1$ is $\ZZ \ast \ZZ$ by van Kampen's theorem, and the universal cover is the $4$-valent Cayley graph of $\ZZ\ast\ZZ$:

![The universal cover of $S^1 \vee S^1$](../../../../assets/assets/Topology/figures/image_2021-01-10-13-19-32.png)

[@Hat02, p. 58] draws further covering spaces of $S^1\vee S^1$.

:::

[[C-ILVEB]]

::: {.example title="Wedge of projective spaces"}
The fundamental group of $\RP^2 \vee \RP^2$ is $\ZZ/2 \ast \ZZ/2$, and the universal cover is an infinite chain of copies of $S^2$, each attached to its two neighbors at antipodal points:

![Another universal cover.](../../../../assets/assets/Topology/figures/image_2021-01-10-13-14-27.png)

:::

::: {.example title="$\RP^2 \wedgeprod T^2$"}
The fundamental group of $\RP^2 \vee T^2$ is $\ZZ/2 \ast \ZZ^2$.
In the tree describing the universal cover, each red vertex is a copy of $S^2$ covering $\RP^2$ and has $2$ neighbors, and each blue vertex is a copy of $\RR^2$ covering $\TT^2$ and has countably many neighbors, one for each point of $\ZZ^2$.

![Universal cover of $\TT^2 \vee \RP^2$](../../../../assets/assets/Topology/figures/tree_cover.png)

:::

### Applications

[[T-TQ4J3]]

::: {.proof}
If $X$ is contractible, there is a homotopy $H\colon X\cross I \to X$ from $\id_X$ to the constant map $c\colon x \mapsto x_0$.
Define $H'\colon Y\cross I \to X$ by $H'(y,t)\coloneqq H(f(y),t)$.
Then $H'(y,0)=f(y)$ and $H'(y,1)=x_0$, so $H'$ is a homotopy from $f$ to a constant map.

:::

[[C-GJRYO]]

::: {.proof}
Suppose $f = p \circ \tilde f$ with $\tilde f\colon X\to Z$, $p\colon Z\to Y$, and $Z$ contractible:

\begin{tikzcd}
	&& {Z} \\
	\\
	{X} && {Y}
	\arrow["{p}", from=1-3, to=3-3]
	\arrow["{\tilde f}", from=3-1, to=1-3]
	\arrow["{f}"', from=3-1, to=3-3]
\end{tikzcd}

By [[T-TQ4J3]], there is a homotopy $\tilde H\colon X\cross I \to Z$ from $\tilde f$ to a constant map $x\mapsto z_0$.
Then $p\circ \tilde H\colon X \cross I \to Y$ is a homotopy from $f$ to the constant map $x\mapsto p(z_0)$.

:::

[[PR-TRSHQ]]

::: {.proof}
Suppose $p\colon\RP^2\to\TT^2$ is a covering map.
By [[PR-R5EN3]], $p_*\colon\pi_1(\RP^2)\to\pi_1(\TT^2)$ is injective.
But $\pi_1(\RP^2)\cong\ZZ/2$ has an element of order $2$, and $\pi_1(\TT^2)\cong\ZZ^2$ is torsion-free, a contradiction.

:::

[[T-O44GI]]

::: {.fact}
A one-sheeted covering map $f\colon X\to Y$ is a homeomorphism: it is a bijective local homeomorphism, hence an open continuous bijection.

:::

## Exercises

- [Patrikis's Math 6520 homework 4 (Utah)](https://www.math.utah.edu/~patrikis/6520Spring2018/6520hw4.pdf).
