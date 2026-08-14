# Homology

## Useful Facts

:::{.fact}
$H_0(X)$ is a free abelian group on the set of path components of $X$.
Thus if $X$ is path connected, $H_0(X) \cong \ZZ$.
In general, $H_0(X) \cong \ZZ^{\abs{\pi_0(X)}}$, where $\abs{\pi_0(X)}$ is the number of path components of $X$.

:::

[[PR-B6BB2]]

:::{.remark}
May need some good pair condition?

:::

:::{.example title="Application"}
\[
H_{n}(\bigvee_{k} S^n) = \ZZ^k
.\]

:::

:::{.proof title="?"}
Mayer-Vietoris. 

:::

:::{.warnings}
$H_{k} \qty{ \prod_ \alpha X_ \alpha}$ is **not** generally equal to $\prod_ \alpha \qty{ H_{k} X_ \alpha }$.
The obstruction is due to torsion -- if all groups are torsionfree, then the Kunneth theorem[^kunneth] yields 
\[
H_{k} (A\cross B) = \prod_{i+j=k} H_{i} A \tensor H_{j} B
\]
\[
H_{n}\qty{\prod_{j=1}^k X_{j}} = \bigoplus_{\mathbf{x} \in \mathcal{P}(n,k)} \bigotimes_{i=1}^{k} H_{x_{i}}(X_{i}).
\]

:::

[[T-FBMYQ]]


:::{.fact title="Assorted facts}
\envlist

- $H_{n}(X) = 0 \iff X$ has no $n\dash$cells.
- $C^0 X = \pt \implies d_{1}: C^1 \to C^0$ is the zero map.

:::

## Known Homology

:::{.example title="Spheres"}
\[
H_{i}(S^n) = 
\begin{cases}
\ZZ & i = 0, n
\\
0 & \text{else}.
\end{cases}
\]

:::

:::{.example title="Real Projective Spaces"}

:::

:::{.example title="Complex Projective Spaces"}

:::

:::{.example title="Surfaces"}

:::


## Mayer-Vietoris

:::{.fact title="Useful algebra fact"}
Since $\ZZ$ is free and thus projective, any exact sequence of the form $0 \to \ZZ^n \to A \to \ZZ^m \to 0$ splits and $A\cong \ZZ^{n}\cross \ZZ^m$.

:::

[[T-3VUOH]]

:::{.example title="Application: computing the homology of a connect sum"}
$H_*(A \# B)$: Use the fact that $A\# B = A \union_{S^n} B$ to apply Mayer-Vietoris.

:::

[[PR-6PENU]]

:::{.proof}
Write $X = A \cup B$, the northern and southern hemispheres, so that $A \cap B = S^{n-1}$, the equator. In the LES, we have:

\[
H^{i+1}(S^n) \xrightarrow{} H^i(S^{n-1}) \xrightarrow{} H^iA \oplus H^i B \xrightarrow{} H^i S^n \xrightarrow{} H^{i-1}(S^{n-1}) \xrightarrow{} H^{i-1}A \oplus H^{i-1}B
.\]

But $A, B$ are contractible, so $H^iA= H^iB = 0$, so we have

\[
H^{i+1}(S^n) \xrightarrow{} H^{i}(S^{n-1}) \xrightarrow{} 0 \oplus 0 \xrightarrow{}H^i(S^n) \xrightarrow{} H^{i-1}(S^{n-1}) \xrightarrow{} 0
.\]

In particular, we have the shape $0 \to A \to B \to 0$ in an exact sequence, which is always an isomorphism.

:::

## More Exact Sequences

[[T-TZ3X7]]

[[T-2W5WN]]

:::{.remark}
Might need assumptions: finite CW complex?

:::

## Relative Homology

:::{.fact title="Some assorted facts"}
\envlist

- $H_{n}(X/A) \cong \tilde H_{n}(X, A)$ when $A\subset X$ has a neighborhood that deformation retracts onto it.

- LES of a pair
  - $(A \injects X) \mapsto (A, X, X/A)$

- For CW complexes $X = \theset{X^{(i)}}$, we have 
\[
H_{n}(X^{(k)},X^{(k-1)}) \cong \begin{cases}\ZZ[\theset{e^n}]~ &k=n,\\ 0 &\text{otherwise}\end{cases} \qquad\text{ since } X^k/X^{k-1} \cong \bigvee S^k
\]
- $H_{n}(X, A) \cong_? H_{n}(X/A, \pt)$

:::


## Exercises

[[P-S7WVQ]]

[[E-AUAOC]]


[^kunneth]: The generalization of Kunneth is as follows: write $\mathcal{P}(n, k)$ be the set of partitions of $n$ into $k$ parts, i.e. $\mathbf{x} \in \mathcal{P}(n,k) \implies \mathbf{x} = (x_{1}, x_{2}, \ldots, x_{k})$ where $\sum x_{i}  = n$. Then
