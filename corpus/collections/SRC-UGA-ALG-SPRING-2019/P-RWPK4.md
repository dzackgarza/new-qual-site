---
schema: qual/card@1
id: P-RWPK4
kind: problem
title: Jordan form over $\QQ$ and $\FF_p$ of the $p\times p$ matrix with zeros on
  the diagonal and ones elsewhere
classification:
  areas:
  - algebra
  topics:
  - Jordan Canonical Form
  - Eigenvalues and Eigenvectors
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the single container states why its subclaims suffice, and the 13
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. Two
    steps, the transformation matrix over $\QQ$ and the Jordan basis over $\FF_p$, had their content in a
    bullet list after the step closed; each now carries its own justification and the bullets are left in
    place. The mathematics is unchanged: $A=J_p-I_p$ shifts the spectrum of the all-ones matrix by $-1$,
    over $\QQ$ the eigenvalues $p$ and $0$ with the $u_i$ spanning the $0$-eigenspace make $A$
    diagonalizable, and over $\FF_p$ the collapse $p-1\equiv-1$ gives a single eigenvalue $-1$ with
    minimal polynomial $(x+1)^2$ and kernel dimension $p-1$, so the block sizes are $2,1,\ldots,1$.
    Checked against the statement on the card, from the UGA Spring 2019 algebra qualifying exam. Nothing
    in the statement was changed.

---
::: {.problem}
Let $p$ be a prime number, and let $A \in M_p(F)$ be the $p \times p$ matrix with $0$ on the main diagonal and $1$ in all off-diagonal entries:
$$
A = \begin{pmatrix}
0 & 1 & 1 & \cdots & 1 \\
1 & 0 & 1 & \cdots & 1 \\
1 & 1 & 0 & \cdots & 1 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & 1 & 1 & \cdots & 0
\end{pmatrix}.
$$
Determine the Jordan Canonical Form (JCF) of $A$ and an explicit change-of-basis matrix $P$ putting $A$ in Jordan canonical form:

(a) When $F = \QQ$,

(b) When $F = \FF_p$.
:::

::: {.solution}

::: pf

::: pf-step

If $J_p$ is the all-ones matrix, then $A=J_p-I_p$.

::: pf-proof

::: pf-step

Let $J_p \in M_p(F)$ denote the $p \times p$ all-ones matrix ($J_{i, j} = 1$ for all $1 \le i, j \le p$).


::: pf-proof
This is a definition: the matrix all of whose entries are $1$.
:::

:::

::: pf-step

Then $A = J_p - I_p$.


::: pf-proof
The off-diagonal entries of $J_p-I_p$ are $1$ and its diagonal entries are $1-1=0$, which is the matrix $A$.
:::

:::

::: pf-step

For any scalar $\mu \in F$ and vector $v \in F^p$:
    $$J_p v = \mu v \iff A v = (J_p - I_p) v = (\mu - 1) v.$$


::: pf-proof
Since $A=J_p-I_p$ one has $Av=J_pv-v$, so the two equations are equivalent.
:::

:::

::: pf-step

Thus the eigenvalues of $A$ are $\lambda = \mu - 1$, where $\mu$ is an eigenvalue of $J_p$, and the corresponding eigenspaces are identical.


::: pf-proof
The equivalence just proved shows that the eigenvectors of $A$ are exactly those of $J_p$, with every eigenvalue shifted by $-1$.
:::

:::

:::

:::

::: pf-step

Over $\QQ$, the matrix $A$ is diagonalizable with eigenvalues $p-1$ and $-1$ of multiplicities $1$ and $p-1$, respectively.

::: pf-proof

::: pf-step

Spectrum of $J_p$:
        - For the vector $v_1 = (1, 1, \dots, 1)^t \in \QQ^p$, $J_p v_1 = p v_1$, so $\mu_1 = p$ is an eigenvalue of $J_p$.
        - For each $i \in \{1, \dots, p-1\}$, let $u_i = e_1 - e_{i+1} = (1, 0, \dots, -1, \dots, 0)^t$. Since the sum of entries of $u_i$ is $1 - 1 = 0$, $J_p u_i = 0 = 0 \cdot u_i$.
        - The $p-1$ vectors $\{u_1, \dots, u_{p-1}\}$ are linearly independent: if $\sum_{i=1}^{p-1} c_i u_i = 0$, the $(i+1)$-st component is $-c_i = 0$ for each $i$.
        - Thus $\mu_0 = 0$ is an eigenvalue of $J_p$ with geometric multiplicity $p - 1$.


::: pf-proof
The three bullets exhibit the spectrum: $v_1$ is an eigenvector with eigenvalue $p$, the $u_i$ are independent eigenvectors with eigenvalue $0$, and the independence computation identifies the $0$-eigenspace as $(p-1)$-dimensional.
:::

:::

::: pf-step

Eigenvalues and eigenspaces of $A$:
        - The eigenvalue $\mu_1 = p$ corresponds to $\lambda_1 = p - 1$ for $A$ with eigenvector $v_1$.
        - The eigenvalue $\mu_0 = 0$ corresponds to $\lambda_0 = -1$ for $A$ with $(p-1)$-dimensional eigenspace spanned by $\{u_1, \dots, u_{p-1}\}$.


::: pf-proof
Shifting the eigenvalues of $J_p$ down by $1$ gives those of $A$, and the eigenspaces do not change.
:::

:::

::: pf-step

Diagonalizability:
        - The sum of geometric multiplicities is $1 + (p - 1) = p = \dim \QQ^p$.
        - Therefore $A$ is diagonalizable over $\QQ$, so its JCF is diagonal:
        $$J_{\QQ}(A) = \operatorname{diag}(p - 1, -1, -1, \dots, -1).$$


::: pf-proof
The geometric multiplicities sum to $p$, the dimension of the space, so the eigenvectors span it and $A$ is diagonalizable; the Jordan form of a diagonalizable matrix is diagonal with the eigenvalues on its diagonal.
:::

:::

::: pf-step

Transformation matrix $P$:


::: pf-proof
The columns are the eigenvector $v_1$ and the independent family $u_i$, so $P$ is invertible, and conjugating $A$ by it produces the diagonal matrix displayed.
:::

:::

- Define $P \in \operatorname{GL}_p(\QQ)$ with columns given by the eigenbasis:
$$P = \begin{pmatrix} v_1 & u_1 & u_2 & \cdots & u_{p-1} \end{pmatrix} = \begin{pmatrix}
1 & 1 & 1 & \cdots & 1 \\
1 & -1 & 0 & \cdots & 0 \\
1 & 0 & -1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & 0 & 0 & \cdots & -1
\end{pmatrix}.$$
- Then $P^{-1} A P = J_{\QQ}(A)$.

:::

:::

::: pf-step

Over $\FF_p$, the nilpotent part $A+I_p$ has square zero and rank one.

::: pf-proof

::: pf-step

Characteristic polynomial over $\FF_p$:
        - In $\FF_p$, $p - 1 \equiv -1 \pmod p$.
        - Thus $\chi_A(x) = (x - (p - 1))(x + 1)^{p-1} \equiv (x + 1)^p \pmod p$.
        - The only eigenvalue of $A$ in $\FF_p$ is $\lambda = -1$, with algebraic multiplicity $p$.


::: pf-proof
The eigenvalues of $A$ over $\QQ$ are $p-1$ and $-1$; reducing coefficients modulo $p$ turns $p-1$ into $-1$, so the characteristic polynomial becomes $(x+1)^p$ and $-1$ is the only eigenvalue.
:::

:::

::: pf-step

Nilpotent part $N = A - (-1) I_p = A + I_p = J_p$:
        - Over $\FF_p$, $N^2 = J_p^2 = p J_p \equiv 0 \in M_p(\FF_p)$.
        - Since $J_p \ne 0$, the minimal polynomial of $A$ is $m_A(x) = (x + 1)^2$.
        - Thus the largest Jordan block has size 2.


::: pf-proof
$J_p^2=pJ_p\equiv0$ in characteristic $p$ and $J_p\neq0$, so $(x+1)^2$ annihilates $A$ while $(x+1)$ does not; the minimal polynomial is therefore $(x+1)^2$, which makes the largest Jordan block of size $2$.
:::

:::

::: pf-step

Geometric multiplicity:
        - All rows of $J_p$ are identical and non-zero, so $\operatorname{rank}(J_p) = 1$.
        - By Rank-Nullity, $\dim \ker(A + I_p) = \dim \ker(J_p) = p - 1$.
        - There are exactly $p - 1$ Jordan blocks for $\lambda = -1$.


::: pf-proof
The rows of $J_p$ are equal and non-zero, so its rank is $1$; rank-nullity gives $\dim\ker(J_p)=p-1$, and that is the number of Jordan blocks for the eigenvalue $-1$.
:::

:::

::: pf-step

Jordan block structure:
        - Since the partition of $p$ into $p - 1$ parts with largest part 2 is uniquely $2 + 1 + 1 + \dots + 1$, the JCF over $\FF_p$ consists of one $2 \times 2$ block and $p - 2$ blocks of size $1 \times 1$:
        $$J_{\FF_p}(A) = \begin{pmatrix}
        -1 & 1 & 0 & \cdots & 0 \\
        0 & -1 & 0 & \cdots & 0 \\
        0 & 0 & -1 & \cdots & 0 \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & 0 & \cdots & -1
        \end{pmatrix}.$$


::: pf-proof
A partition of $p$ into $p-1$ parts whose largest part is $2$ must be $2+1+\cdots+1$, and a partition of the size of each block determines the Jordan form.
:::

:::

::: pf-step

Jordan basis and matrix $P$:


::: pf-proof
The chain $w\mapsto v_1\mapsto0$ spans a $2$-dimensional block, the $u_i$ are fixed eigenvectors, and $2+(p-2)=p$ shows the set is a basis; in that basis the matrix of $A$ is the displayed Jordan form.
:::

:::

- Choose the generalized eigenvector $w = e_1 = (1, 0, 0, \dots, 0)^t \in \FF_p^p$.
- Apply $A + I = J_p$:
$$(A + I) w = J_p e_1 = (1, 1, \dots, 1)^t = v_1.$$
- Since $(A + I) v_1 = J_p v_1 = p v_1 \equiv 0$, the pair $\{v_1, w\}$ forms a Jordan chain of length 2:
$$A v_1 = -v_1, \qquad A w = v_1 - w.$$
- For the remaining $p - 2$ blocks of size 1, choose eigenvectors $u_1, \dots, u_{p-2}$ where $u_i = e_1 - e_{i+1}$.
- These $p$ vectors $\{v_1, w, u_1, u_2, \dots, u_{p-2}\}$ form a basis of $\FF_p^p$.
- Setting $P = \begin{pmatrix} v_1 & w & u_1 & u_2 & \cdots & u_{p-2} \end{pmatrix} \in \operatorname{GL}_p(\FF_p)$ satisfies $P^{-1} A P = J_{\FF_p}(A)$.

:::

:::

::: pf-qed

Over $\QQ$, $A$ is diagonalizable with eigenvalues $p-1$ (mult 1) and $-1$ (mult $p-1$). Over $\FF_p$, $A$ has one Jordan block of size 2 and $p-2$ Jordan blocks of size 1 for eigenvalue $-1$.

:::

:::

:::
