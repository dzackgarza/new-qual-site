---
schema: qual/card@1
id: P-AGH398TONEMODULE
kind: problem
title: The module $T^1$ classifies infinitesimal deformations of an algebra
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Infinitesimal Deformations
  - Sheaves of Differentials
  - Dual Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.9.8 and Exercise II.8.6 in Hartshorne. The proof first
    lifts a polynomial presentation of A across a first-order deformation,
    identifies the resulting embedded deformation with an element of
    Hom_A(J/J^2,A), and then checks that changing the chosen lift changes this
    element exactly by the restriction of a derivation of P.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $A$ be a finitely generated $k\dash$algebra. Write $A$ as a quotient of a polynomial ring $P$ over $k$, and let $J$ be the kernel:
\[
0 \to J \to P \to A \to 0
.\]
Consider the exact sequence of (II, 8.4A),
\[
J/J^2 \to \Omega_{P/k} \tensor_P A \to \Omega_{A/k} \to 0
.\]
Apply the functor $\Hom_A(\cdot, A)$, and let $T^1(A)$ be the cokernel:
\[
\Hom_A(\Omega_{P/k} \tensor A, A) \to \Hom_A(J/J^2, A) \to T^1(A) \to 0
.\]

Now use the construction of (II, Ex. 8.6) to show that $T^1(A)$ classifies infinitesimal deformations of $A$, that is, algebras $A'$ flat over $D = k[t]/t^2$ with $A' \tensor_D k \cong A$. It follows that $T^1(A)$ is independent of the given representation of $A$ as a quotient of a polynomial ring $P$.
:::

::: {.solution}
Write
$$
D=k[\epsilon]/(\epsilon^2),
\qquad
P_D=P\tensor_kD.
$$
An infinitesimal deformation is understood together with an identification
$A'/\epsilon A'\cong A$, and two deformations are identified when there is a
$D$-algebra isomorphism inducing the identity on $A$.

<1>1. Every infinitesimal deformation $A'$ of $A$ admits a surjective $D$-algebra map
$$
q':P_D\surjects A'
$$
whose reduction modulo $\epsilon$ is the fixed quotient $q:P\surjects A$.

::: {.proof}
By the infinitesimal lifting property of Exercise II.8.6, the map
$$
q:P\longrightarrow A=A'/\epsilon A'
$$
lifts to a $k$-algebra map
$$
\widetilde q:P\longrightarrow A'.
$$
Together with the structure map $D\to A'$, this gives a $D$-algebra map
$$
q':P_D\longrightarrow A'.
$$

It is surjective. Indeed, let $a'\in A'$. Its reduction in $A$ is $q(p)$ for
some $p\in P$, so
$$
a'-\widetilde q(p)\in\epsilon A'.
$$
Write this difference as $\epsilon b'$. If $q(r)$ is the reduction of $b'$,
then
$$
\epsilon b'=\epsilon\widetilde q(r),
$$
because $b'-\widetilde q(r)\in\epsilon A'$ and $\epsilon^2=0$.
Hence
$$
a'=q'(p+\epsilon r).
$$
:::

<1>2. If $J'=\ker q'$, then $J'$ is an embedded first-order deformation of the ideal $J\subseteq P$, and therefore determines an element
$$
\phi_{q'}\in\Hom_A(J/J^2,A).
$$

::: {.proof}
Reduction of $q'$ modulo $\epsilon$ is $q$, so
$$
(J'+(\epsilon))/(\epsilon)=J.
$$
Since $A'=P_D/J'$ is flat over $D$, the dual-number flatness criterion gives
$$
J'\cap\epsilon P=\epsilon J.
$$
Thus, for each $j\in J$, choose a lift
$$
j+\epsilon p\in J'.
$$
The class of $p$ in $A=P/J$ depends only on $j\bmod J^2$, and the assignment
$$
j\bmod J^2\longmapsto p\bmod J
$$
is $A$-linear. This is exactly the embedded-deformation construction of
[[P-AGH397INFDEFSUB|Exercise III.9.7]], applied to
$$
\Spec A\subseteq\Spec P.
$$
It yields $\phi_{q'}\in\Hom_A(J/J^2,A)$.
:::

<1>3. Conversely, every
$$
\phi\in\Hom_A(J/J^2,A)
$$
determines an infinitesimal deformation
$$
A_\phi=P_D/J_\phi,
$$
where
$$
J_\phi
=\{j+\epsilon p:j\in J,\ p\bmod J=\phi(j\bmod J^2)\}.
$$

::: {.proof}
Exercise III.9.7 shows that $J_\phi$ is an ideal of $P_D$, that
$$
(J_\phi+(\epsilon))/(\epsilon)=J,
$$
and that
$$
J_\phi\cap\epsilon P=\epsilon J.
$$
Therefore $A_\phi=P_D/J_\phi$ is flat over $D$, and its special fibre is
$$
A_\phi\tensor_Dk\cong P/J=A.
$$
Hence $A_\phi$ is an infinitesimal deformation of $A$.
:::

<1>4. If $q'_1,q'_2:P_D\surjects A'$ are two lifts of the same quotient map $q:P\surjects A$ to one deformation $A'$, then
$$
\phi_{q'_2}-\phi_{q'_1}
$$
lies in the image of
$$
\Hom_A(\Omega_{P/k}\tensor_PA,A)
\longrightarrow
\Hom_A(J/J^2,A).
$$

::: {.proof}
For $p\in P$, the two lifts have the same reduction modulo $\epsilon$, so there
is a unique element $\delta(p)\in A$ such that
$$
q'_2(p)-q'_1(p)=\epsilon\delta(p).
$$
Flatness of $A'$ identifies $\epsilon A'$ with $A$ via
$$
a\longmapsto\epsilon\widetilde a,
$$
so $\delta$ is well defined. Comparing products shows
$$
\delta(pp')=q(p)\delta(p')+q(p')\delta(p),
$$
and therefore $\delta:P\to A$ is a $k$-derivation.
By the universal property of Kähler differentials, it corresponds to an
$A$-linear map
$$
\theta_\delta:\Omega_{P/k}\tensor_PA\longrightarrow A.
$$

For $j\in J$, choose
$$
j+\epsilon p\in\ker q'_1.
$$
Then
$$
q'_2(j+\epsilon p)
=\epsilon\bigl(\delta(j)+q(p)\bigr).
$$
Thus replacing the lift $q'_1$ by $q'_2$ changes the homomorphism
$J/J^2\to A$ by minus the restriction of the derivation $\delta$, namely by the
negative of the image of $\theta_\delta$ under
$$
\Hom_A(\Omega_{P/k}\tensor_PA,A)
\longrightarrow
\Hom_A(J/J^2,A).
$$
In particular, the two homomorphisms have the same class in the cokernel.
:::

<1>5. Conversely, if two elements
$$
\phi_1,\phi_2\in\Hom_A(J/J^2,A)
$$
differ by the restriction of a derivation $\delta:P\to A$, then the deformations
$A_{\phi_1}$ and $A_{\phi_2}$ are isomorphic over $D$ by an isomorphism inducing the identity on $A$.

::: {.proof}
Choose polynomial generators $x_1,\ldots,x_m$ of $P$ and choose lifts
$h_i\in P$ of the elements $\delta(x_i)\in A$.
Define a $D$-algebra automorphism
$$
\alpha:P_D\longrightarrow P_D,
\qquad
x_i\longmapsto x_i+\epsilon h_i,
\qquad
\epsilon\longmapsto\epsilon.
$$
Its inverse is obtained by replacing $\epsilon h_i$ with $-\epsilon h_i$, so
$\alpha$ reduces to the identity on $P$ modulo $\epsilon$.

For $j\in J$,
$$
\alpha(j)\equiv j+\epsilon\delta(j)\pmod{\epsilon J}.
$$
Hence, if $\phi_2-\phi_1$ is the restriction of $\delta$, the defining formula
for the ideals in step <1>3 gives
$$
\alpha(J_{\phi_1})=J_{\phi_2}
$$
exactly.
Therefore $\alpha$ descends to a $D$-algebra isomorphism
$$
A_{\phi_1}\iso A_{\phi_2}
$$
which induces the identity on the special fibre $A$.
:::

<1>6. Two elements of $\Hom_A(J/J^2,A)$ determine isomorphic infinitesimal deformations if and only if they have the same image in $T^1(A)$.

::: {.proof}
Steps <1>4 and <1>5 show that changing a polynomial lift, or equivalently
changing the presentation of the same deformation inside $\Spec P_D$, changes
the embedded-deformation class precisely by an element in the image of
$$
\Hom_A(\Omega_{P/k}\tensor_PA,A).
$$

Conversely, suppose
$$
\Psi:A_{\phi_1}\iso A_{\phi_2}
$$
is a $D$-algebra isomorphism inducing the identity on $A$.
Compose the quotient map $P_D\to A_{\phi_1}$ with $\Psi$.
This gives a second lift of $P\to A$ to $A_{\phi_2}$.
Its kernel is $J_{\phi_1}$, while the standard quotient
map has kernel $J_{\phi_2}$.
Step <1>4 therefore shows that $\phi_1$ and $\phi_2$ differ by the image of a
derivation of $P$.

Thus the set of isomorphism classes is exactly the cokernel
$$
\operatorname{coker}\!\left(
\Hom_A(\Omega_{P/k}\tensor_PA,A)
\longrightarrow
\Hom_A(J/J^2,A)
\right).
$$
:::

<1>7. The infinitesimal deformations of $A$ are classified by
$$
\boxed{T^1(A)}.
$$

::: {.proof}
By definition, the cokernel displayed in step <1>6 is $T^1(A)$.
Steps <1>1--<1>3 associate an element of that cokernel to every deformation and
construct a deformation from every representative, while steps <1>4--<1>6 show
that precisely the representatives in one cokernel class give isomorphic
deformations.
:::

<1>8. The module $T^1(A)$ is independent of the chosen polynomial presentation of $A$.

::: {.proof}
Step <1>7 identifies $T^1(A)$ intrinsically with the set of first-order
deformations of the $k$-algebra $A$ up to isomorphism fixing the special fibre.
This classification depends only on $A$, not on a presentation
$P\surjects A$.
Hence the classifying module denoted $T^1(A)$ is independent, up to the
canonical identification supplied by deformation classes, of the chosen
polynomial presentation.
:::

<1>9. Q.E.D.

::: {.proof}
Steps <1>1--<1>7 prove the classification, and step <1>8 gives the stated
independence of the polynomial presentation.
:::
:::
