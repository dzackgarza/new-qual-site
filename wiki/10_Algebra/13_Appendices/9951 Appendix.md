---
order: 9951
---

# Appendix: Extra Topics

[[PR-NESS4]]

[[D-43MDF]]

## Characteristic Subgroups

:::{.slogan}
Normality is not transitive!

I.e. if $H\normal G$ and $N\normal H$, it's not necessarily the case that $N\normal G$.

:::

[[D-53LTN]]

:::{.remark title="Characteristic isn't equivalent to normalcy"}
Characteristic subgroups are normal, because $\psi_g(\wait) \da g(\wait)g\inv$ is an (inner) automorphic of $G$.
Not every normal subgroup is characteristic: take $G \da H_1 \cross H_2$ and $\psi(x, y) = (y, x)$.

:::

[[PR-IOMVN]]

:::{.proof title="?"}
$A \ch B \normal C \implies A\normal C$:

- $A\ch B$ iff $A$ is fixed by every $\psi\in \Aut(B)$., WTS $cAc\inv = A$ for all $c\in C$.
- Since $B\normal C$, the automorphism $\psi(\wait) \da c(\wait)c\inv$ descends to an element of $\Aut(B)$.
- Then $\psi(A) = A$ since $A\ch B$, so $cAc\inv = A$ and $A\normal C$.

:::

[[PR-GJLQP]]

:::{.proof title="?"}
Let $\psi \in \Aut(H)$ and $x=\psi(y)\in \psi(Z(H))$ so $y\in Z(H)$, then for arbitrary $h\in H$,
\[
\psi(y)h 
&= \psi(y) (\psi \circ \psi\inv)(h) \\
&= \psi( y \cdot \psi\inv(h) ) \\
&= \psi( \psi\inv(h) \cdot y ) && \text{since } \psi\inv(h)\in H, \, y\in Z(H) \\
&= h\psi(y)
.\]

:::

## Normal Closures and Cores

[[D-BPRD3]]

[[D-QMVEB]]

[[T-4XKGD]]

### Exercises

[[P-5UUNM]]

## Nilpotent Groups

[[D-53JVH]]

> Moral: the adjoint map is nilpotent.

[[T-7PU33]]

[[T-4INET]]

[[T-GM7EB]]

[[T-OHEFT]]

:::{.proposition}
For $G$ a finite group, TFAE:

- $G$ is nilpotent
- Normalizers grow, i.e. if $H < G$ is proper then $H < N_G(H)$.
- Every Sylow-p subgroup is normal
- $G$ is the direct product of its Sylow p-subgroups
- Every maximal subgroup is normal
- $G$ has a terminating *Lower* Central Series
- $G$ has a terminating *Upper* Central Series

:::

:::{.fact}
\envlist

- Nilpotent groups satisfy the 2 out of 3 property.
- $G$ has normal subgroups of order $d$ for *every* $d$ dividing $\abs{G}$

:::

## Rings

[[D-DU4UQ]]

:::{.example title="Why care about Gorenstein rings?"}
If $R\in \gr\kAlg$ with $\dim_k R < \infty$, then $R$ decomposes as $R = R_0 \oplus R_1 \oplus \cdots R_n$ with $R_0 \da k$, and $R$ is Gorenstein iff $R$ satisfies "Poincaré duality": $\dim_k R_0 = \dim_k R_m = 1$ and there is a perfect pairing $R_i \tensor_k R_{n-j} \to R_n$.

:::
