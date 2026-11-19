---
schema: qual/card@1
id: P-APAS21H
kind: problem
title: Character table of $A_4$ and the Wedderburn decomposition of $\CC[A_4]$
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Character Theory
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Added the class computation with its
    reason (the three double transpositions are conjugate inside A4, exhibited by two conjugations,
    and the eight 3-cycles split into two classes of four because the centralizer in A4 has order
    3); the three linear characters are the inflations from A4/V4 = C3, with V4 normal because it is
    a union of classes; the fourth degree is forced by 1+1+1+d^2 = 12; and chi_4 is identified as
    the permutation character minus the trivial one, with its three values computed, and its
    irreducibility checked by <chi_4,chi_4> = (9+3+0+0)/12 = 1. The table's consistency is now a
    step: the row and column orthogonality computations are displayed, including the mixed inner
    product 4 + 4(omega + omega^2) = 0. The Wedderburn step states Maschke and the indexing by
    irreducible characters, and the conclusion notes the uniqueness up to order. The card's answer,
    r = 4 and (1,1,1,3), is unchanged; the card says the argument is its own.
---

::: {.problem}
Find the character table of the alternating subgroup $A_4$ of the symmetric group $S_4$.
The group algebra of $A_4$ is isomorphic to a direct sum
$$
\CC[A_4] \cong \operatorname{Mat}_{n_1}(\CC) \oplus \cdots \oplus \operatorname{Mat}_{n_r}(\CC)
$$
of matrix algebras over $\CC$.
Determine $r$ and the numbers $n_1, \dots, n_r > 0$.
:::

::: {.solution}
$A_4$ has four conjugacy classes — the identity, the three double transpositions, and the eight $3$-cycles split into two classes of four — so it has four irreducible characters. Three are the inflations of the characters of $A_4/V_4\cong C_3$ and are linear; the fourth is the standard character of degree $3$, the permutation character less the trivial one. The degrees satisfy $1+1+1+9=12$, which checks the list, and the Wedderburn decomposition then has one matrix algebra per irreducible character. The argument is this card's own: no retained solution set covers this exam.

::: pf

::: {.pf-step #classes}
The conjugacy classes of $A_4$ are $C_1=\{1\}$, $C_2$ the three double transpositions, and two classes $C_3$, $C_4$ of four $3$-cycles each, with $C_4=C_3^{-1}$; so there are four irreducible characters.

::: pf-proof
The identity is its own class. The three double transpositions $(12)(34),(13)(24),(14)(23)$ are conjugate in $A_4$: conjugating $(12)(34)$ by $(123)$ gives $(14)(23)$, and by $(124)$ gives $(13)(24)$, and all three are in $A_4$. A $3$-cycle is fixed by no odd permutation in the sense that the $S_4$-class of $3$-cycles, of size $8$, splits into two $A_4$-classes of size $4$, since the centralizer of a $3$-cycle in $A_4$ is the cyclic group it generates, of order $3$, and $\abs{A_4}/\abs{C_{A_4}(\sigma)}=12/3=4$; $C_3=\{(123),(134),(142),(243)\}$ is one class and $C_4$ the class of inverses. A finite group has as many irreducible characters over $\CC$ as conjugacy classes, so four.
:::

:::


::: {.pf-step #linear}
$V_4=\{1,(12)(34),(13)(24),(14)(23)\}$ is normal in $A_4$ with $A_4/V_4\cong C_3$, and inflating the three characters of $C_3$ gives three distinct linear characters of $A_4$.

::: pf-proof
$V_4$ is a union of conjugacy classes ($\{1\}$ and $C_2$) and is a subgroup of order $4$, hence normal; the quotient has order $12/4=3$, so it is cyclic of order $3$. A character $\psi$ of the quotient pulls back to $\chi(g)=\psi(gV_4)$, which is a homomorphism $A_4\to\CC^\times$, i.e. a linear character; distinct $\psi$ give distinct $\chi$ since $g\mapsto gV_4$ is onto.
:::

:::


::: {.pf-step #degree3}
The fourth irreducible character has degree $3$, and $\sum_\chi\chi(1)^2=12$ reads $1+1+1+9$.

::: pf-proof
The degrees $d_i$ of the irreducible characters satisfy $\sum_id_i^2=\abs{A_4}=12$, and three of them are $1$. So $d_4^2=12-3=9$ and $d_4=3$.
:::

:::


::: {.pf-step #standard}
Let $\pi$ be the permutation character of $A_4$ on $\{1,2,3,4\}$ and $\chi_4=\pi-\mathbf1$; then $\chi_4$ is irreducible of degree $3$ and takes the values $3$ at $1$, $-1$ on $C_2$, $0$ on $C_3\cup C_4$.

::: pf-proof
$\pi$ is the character of the permutation module $\CC^4$, which contains the trivial line spanned by $(1,1,1,1)$ as a direct summand (the span is invariant and has an invariant complement, the sum-zero vectors, since the standard inner product is $A_4$-invariant); the complement has dimension $3$ and character $\pi-\mathbf1$. Its values: at the identity $\pi=4$, so $\chi_4(1)=3$; a double transposition fixes no point, so $\pi=0$ and $\chi_4=-1$; a $3$-cycle fixes exactly one point, so $\pi=1$ and $\chi_4=0$. Hence $\langle\chi_4,\chi_4\rangle=\frac1{12}(9+3\cdot1+0+0)=1$, so $\chi_4$ is irreducible.
:::

:::


::: {.pf-step #table}
Setting $\chi_2((123))=\omega$, $\chi_2((134))=\omega$, $\chi_2((142))=\omega$ and $\chi_3=\overline{\chi_2}$ gives the table displayed in the statement.

::: pf-proof
On $C_3$ the quotient $A_4/V_4\cong C_3$ identifies a $3$-cycle with a generator of $C_3$, and the two nontrivial characters of $C_3$ take the value $\omega=e^{2\pi i/3}$ and $\omega^2$ there; so one of $\chi_2,\chi_3$ is $\omega$ and the other $\omega^2$ on $C_3$. On $C_4=C_3^{-1}$ the values are the complex conjugates, since $\chi(g^{-1})=\overline{\chi(g)}$ for a character of finite order; that gives $\omega^2$ and $\omega$ respectively. All three linear characters are $1$ on $C_1$ and on $C_2\subseteq V_4$. With step [](#standard){.pf-ref} this is exactly the displayed array, and $\chi_4$ has the same value on $C_3$ and $C_4$ because it is real, $0$ on both.
:::

:::


::: {.pf-step #check}
The table is consistent: rows are orthonormal, and columns are orthogonal.

::: pf-proof
$\langle\chi_2,\chi_2\rangle=\frac1{12}(1+3\cdot1+4\cdot\omega\bar\omega+4\cdot\bar\omega\omega)=\frac1{12}(4+4+4)=1$, and similarly for $\chi_3$. For the mixed inner product, $\chi_2\overline{\chi_3}$ takes the value $1$ on $C_1$, $1$ on $C_2$, $\omega\cdot\omega=\omega^2$ on $C_3$ (since $\overline{\chi_3}=\omega$ there) and $\omega^2\cdot\omega^2=\omega$ on $C_4$, so the weighted sum is $1+3\cdot1+4\omega^2+4\omega=4+4(\omega+\omega^2)=4-4=0$, using $\omega+\omega^2=-1$. So the two are orthogonal, and both are orthogonal to $\chi_4$ and to $\mathbf1$ by the values above.
:::

:::


::: {.pf-step #wedderburn}
$\CC[A_4]\cong\bigoplus_{\chi\in\operatorname{Irr}(A_4)}\operatorname{Mat}_{\chi(1)}(\CC)$, hence $\CC[A_4]\cong\CC\oplus\CC\oplus\CC\oplus\operatorname{Mat}_3(\CC)$.

::: pf-proof
$\CC$ is a splitting field for the finite group $A_4$ (all irreducible characters are realizable over $\CC$ by definition of the group algebra over $\CC$), and Maschke's theorem makes $\CC[A_4]$ semisimple, since $\abs{A_4}=12$ is invertible in $\CC$. By Wedderburn's structure theorem the group algebra is a product of matrix algebras over $\CC$, one for each irreducible representation, with the size equal to the degree; the degrees are $1,1,1,3$ by steps [](#linear){.pf-ref} and [](#degree3){.pf-ref}.
:::

:::


::: {.pf-step #conclusion}
$r=4$ and, up to order, $(n_1,n_2,n_3,n_4)=(1,1,1,3)$.

::: pf-proof
Step [](#wedderburn){.pf-ref} exhibits four matrix algebras of sizes $1,1,1,3$; the decomposition into simple factors is unique up to order (the factors are the isotypic components, indexed by the irreducible characters), so $r=4$ and the sizes are $1,1,1,3$ in some order. The dimension check $1+1+1+9=12=\dim\CC[A_4]$ confirms it.
:::

:::

:::
:::
