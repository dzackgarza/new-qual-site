---
schema: qual/card@1
id: P-AGH397INFDEFSUB
kind: problem
title: Infinitesimal deformations of a closed subscheme and the normal sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Infinitesimal Deformations
  - Normal Sheaf
  - Dual Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise III.9.7 in Hartshorne and the surrounding flatness discussion for families over one-dimensional bases. The proof gives the affine ideal-theoretic correspondence over the dual numbers, proves the exact flatness criterion directly, identifies the resulting map with Hom(I/I^2,A/I), and then glues the construction to the normal sheaf.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y \subseteq X$ be a closed subscheme, where $X$ is a scheme of finite type over a field $k$. Let $D = k[t]/t^2$ be the ring of dual numbers, and define an infinitesimal deformation of $Y$ as a closed subscheme of $X$ to be a closed subscheme $Y' \subseteq \fiberprod{X}{k}{D}$ which is flat over $D$ and whose closed fibre is $Y$.

Show that these $Y'$ are classified by $H^0(Y, \mcn_{Y/X})$, where
\[
\mcn_{Y/X} = \sheafhom_{\mco_Y}(\mci_Y / \mci_Y^2, \mco_Y)
.\]
:::

::: {.solution}
Write $\epsilon$ for the class of $t$ in
$$
D=k[\epsilon]/(\epsilon^2).
$$
For an affine open $U=\Spec A\subseteq X$, put
$$
I=\Gamma(U,\mci_Y),\qquad A_D=A[\epsilon]/(\epsilon^2).
$$
Then a closed subscheme of $U\times_k\Spec D$ is determined by an ideal $J\subseteq A_D$.

<1>1. Suppose $J\subseteq A_D$ has closed fibre $I$, i.e.
$$
(J+(\epsilon))/(\epsilon)=I\subseteq A.
$$
Then $B=A_D/J$ is flat over $D$ if and only if
$$
\boxed{J\cap \epsilon A=\epsilon I}.
$$

::: {.proof}
First note that $\epsilon I\subseteq J$.
Indeed, for $i\in I$ choose a lift $i+\epsilon a\in J$; multiplying by $\epsilon$ gives $\epsilon i\in J$.

In the quotient $B$, multiplication by $\epsilon$ has kernel
$$
\ker(\epsilon:B\to B)
=\{\bar a+\epsilon\bar b:\epsilon a\in J\}.
$$
The equality $J\cap\epsilon A=\epsilon I$ is therefore equivalent to
$$
\ker(\epsilon:B\to B)=\epsilon B.
$$

This last condition is equivalent to flatness over $D$.
One direction is immediate by tensoring the exact periodic resolution of the residue field $k=D/(\epsilon)$.
Conversely, assume $\ker\epsilon=\epsilon B$.
Choose a $k$-basis $(\bar b_\lambda)$ of $B/\epsilon B$ and lifts $b_\lambda\in B$.
The induced map
$$
\bigoplus_\lambda D\longrightarrow B
$$
is surjective: reduce any element modulo $\epsilon B$, lift the resulting finite linear combination, and then lift once more inside $\epsilon B$.
If
$$
\sum_\lambda (c_\lambda+\epsilon d_\lambda)b_\lambda=0,
$$
reduction modulo $\epsilon B$ gives all $c_\lambda=0$.
Then
$$
\epsilon\sum_\lambda d_\lambda b_\lambda=0,
$$
so $\sum d_\lambda b_\lambda\in\ker\epsilon=\epsilon B$.
Reducing again modulo $\epsilon B$ gives every $d_\lambda=0$.
Thus $B$ is a free, hence flat, $D$-module.
:::

<1>2. A flat deformation ideal $J$ determines a unique homomorphism
$$
\phi_J:I/I^2\longrightarrow A/I.
$$

::: {.proof}
For $i\in I$, choose a lift
$$
i+\epsilon a\in J
$$
and define
$$
\phi_J(i)=a\bmod I.
$$
This is independent of the chosen lift.
If also $i+\epsilon a'\in J$, then
$$
\epsilon(a-a')\in J\cap\epsilon A=\epsilon I
$$
by step <1>1, so $a-a'\in I$.

The construction is additive.
For $c\in A$, multiplying a lift by $c$ gives
$$
ci+\epsilon ca\in J,
$$
hence
$$
\phi_J(ci)=c\phi_J(i)
$$
in $A/I$.
Thus $\phi_J:I\to A/I$ is $A$-linear.
Since $I$ acts trivially on $A/I$, it follows that $\phi_J(I^2)=0$, so it factors uniquely through the $A/I$-linear map
$$
I/I^2\longrightarrow A/I.
$$
:::

<1>3. Conversely, every
$$
\phi\in\operatorname{Hom}_{A/I}(I/I^2,A/I)
$$
determines a flat deformation ideal
$$
J_\phi
=\{i+\epsilon a\in A_D:i\in I,\ a\bmod I=\phi(i\bmod I^2)\}.
$$

::: {.proof}
The set $J_\phi$ is additive.
For $c+\epsilon d\in A_D$ and $i+\epsilon a\in J_\phi$,
$$
(c+\epsilon d)(i+\epsilon a)
=ci+\epsilon(ca+di).
$$
Modulo $I$,
$$
ca+di\equiv c\phi(i)
=\phi(ci),
$$
because $di\in I$ and $\phi$ is $A/I$-linear.
Hence $J_\phi$ is an ideal.

Its reduction modulo $\epsilon$ is exactly $I$, so its closed fibre is $Y\cap U$.
If $\epsilon a\in J_\phi$, then its first component is zero and the defining condition says
$$
a\bmod I=\phi(0)=0.
$$
Thus
$$
J_\phi\cap\epsilon A=\epsilon I.
$$
Step <1>1 shows that $A_D/J_\phi$ is flat over $D$.
Therefore $J_\phi$ defines an infinitesimal embedded deformation of $Y\cap U$ in $U$.
:::

<1>4. The constructions in steps <1>2 and <1>3 are mutually inverse.

::: {.proof}
Starting from $\phi$, the lift $i+\epsilon a\in J_\phi$ satisfies
$$
a\bmod I=\phi(i\bmod I^2),
$$
so step <1>2 recovers exactly $\phi$.

Conversely, let $J$ be flat and put $\phi=\phi_J$.
Every element $i+\epsilon a\in J$ satisfies the defining congruence for $J_\phi$, hence
$$
J\subseteq J_\phi.
$$
For the reverse inclusion, let $i+\epsilon a\in J_\phi$.
Choose $i+\epsilon a'\in J$.
The equality of their images under $\phi$ gives $a-a'\in I$, so
$$
\epsilon(a-a')\in\epsilon I\subseteq J.
$$
Therefore $i+\epsilon a\in J$ and $J_\phi=J$.
:::

<1>5. The affine correspondence is compatible with localization and therefore glues canonically over $X$.

::: {.proof}
Every operation used in steps <1>1--<1>4 commutes with localization: reduction modulo $\epsilon$, the ideal quotient $I/I^2$, the module $A/I$, and the formula defining $J_\phi$.
Thus on overlapping affine opens, the homomorphisms obtained from a global deformation ideal sheaf agree after restriction.
They glue to a global section
$$
\phi_{Y'}\in
H^0\!\left(Y,
\sheafhom_{\mco_Y}(\mci_Y/\mci_Y^2,\mco_Y)
\right).
$$

Conversely, a global section of this sheaf restricts on each affine open to a homomorphism $\phi$ as in step <1>3.
The corresponding ideals $J_\phi$ agree on overlaps by the localization compatibility, so they glue to a quasicoherent ideal sheaf on $X\times_k\Spec D$.
The resulting closed subscheme has closed fibre $Y$ and is flat over $D$ by the local criterion in step <1>1.
:::

<1>6. The set of infinitesimal embedded deformations of $Y$ in $X$ is therefore
$$
\boxed{H^0(Y,\mcn_{Y/X})}.
$$

::: {.proof}
By [[D-MODCONORM|the definition of the normal sheaf]],
$$
\mcn_{Y/X}
=\sheafhom_{\mco_Y}(\mci_Y/\mci_Y^2,\mco_Y).
$$
Step <1>5 gives mutually inverse global constructions between its sections and flat closed subschemes
$$
Y'\subseteq X\times_k\Spec D
$$
whose closed fibre is $Y$.
Hence $H^0(Y,\mcn_{Y/X})$ classifies exactly the infinitesimal deformations requested in the problem.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 establish the affine classification, and steps <1>5--<1>6 globalize it and identify the parameter space with global sections of the normal sheaf.
:::
:::
