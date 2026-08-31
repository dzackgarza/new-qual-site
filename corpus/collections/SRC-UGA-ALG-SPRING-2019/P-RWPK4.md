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
---

::: problem
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

(a) When $F = \mathbb{Q}$,

(b) When $F = \mathbb{F}_p$.
:::

::: solution
**Goal:** Compute the characteristic polynomial, eigenspaces, Jordan canonical forms, and transition matrices of $A$ over $\mathbb{Q}$ in (a) and over $\mathbb{F}_p$ in (b).

<1>1. Relation to the all-ones matrix $J_p$:
    *Proof:*
    <2>1. Let $J_p \in M_p(F)$ denote the $p \times p$ all-ones matrix ($J_{i, j} = 1$ for all $1 \le i, j \le p$).
    <2>2. Then $A = J_p - I_p$.
    <2>3. For any scalar $\mu \in F$ and vector $v \in F^p$:
    $$J_p v = \mu v \iff A v = (J_p - I_p) v = (\mu - 1) v.$$
    <2>4. Thus the eigenvalues of $A$ are $\lambda = \mu - 1$, where $\mu$ is an eigenvalue of $J_p$, and the corresponding eigenspaces are identical.

<1>2. Part (a): JCF and change-of-basis matrix over $\mathbb{Q}$.
    *Proof:*
    <2>1. Spectrum of $J_p$:
        - For the vector $v_1 = (1, 1, \dots, 1)^t \in \mathbb{Q}^p$, $J_p v_1 = p v_1$, so $\mu_1 = p$ is an eigenvalue of $J_p$.
        - For each $i \in \{1, \dots, p-1\}$, let $u_i = e_1 - e_{i+1} = (1, 0, \dots, -1, \dots, 0)^t$. Since the sum of entries of $u_i$ is $1 - 1 = 0$, $J_p u_i = 0 = 0 \cdot u_i$.
        - The $p-1$ vectors $\{u_1, \dots, u_{p-1}\}$ are linearly independent: if $\sum_{i=1}^{p-1} c_i u_i = 0$, the $(i+1)$-st component is $-c_i = 0$ for each $i$.
        - Thus $\mu_0 = 0$ is an eigenvalue of $J_p$ with geometric multiplicity $p - 1$.
    <2>2. Eigenvalues and eigenspaces of $A$:
        - The eigenvalue $\mu_1 = p$ corresponds to $\lambda_1 = p - 1$ for $A$ with eigenvector $v_1$.
        - The eigenvalue $\mu_0 = 0$ corresponds to $\lambda_0 = -1$ for $A$ with $(p-1)$-dimensional eigenspace spanned by $\{u_1, \dots, u_{p-1}\}$.
    <2>3. Diagonalizability:
        - The sum of geometric multiplicities is $1 + (p - 1) = p = \dim \mathbb{Q}^p$.
        - Therefore $A$ is diagonalizable over $\mathbb{Q}$, so its JCF is diagonal:
        $$J_{\mathbb{Q}}(A) = \operatorname{diag}(p - 1, -1, -1, \dots, -1).$$
    <2>4. Transformation matrix $P$:
        - Define $P \in \operatorname{GL}_p(\mathbb{Q})$ with columns given by the eigenbasis:
        $$P = \begin{pmatrix} v_1 & u_1 & u_2 & \cdots & u_{p-1} \end{pmatrix} = \begin{pmatrix}
        1 & 1 & 1 & \cdots & 1 \\
        1 & -1 & 0 & \cdots & 0 \\
        1 & 0 & -1 & \cdots & 0 \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        1 & 0 & 0 & \cdots & -1
        \end{pmatrix}.$$
        - Then $P^{-1} A P = J_{\mathbb{Q}}(A)$.

<1>3. Part (b): JCF and change-of-basis matrix over $\mathbb{F}_p$.
    *Proof:*
    <2>1. Characteristic polynomial over $\mathbb{F}_p$:
        - In $\mathbb{F}_p$, $p - 1 \equiv -1 \pmod p$.
        - Thus $\chi_A(x) = (x - (p - 1))(x + 1)^{p-1} \equiv (x + 1)^p \pmod p$.
        - The only eigenvalue of $A$ in $\mathbb{F}_p$ is $\lambda = -1$, with algebraic multiplicity $p$.
    <2>2. Nilpotent part $N = A - (-1) I_p = A + I_p = J_p$:
        - Over $\mathbb{F}_p$, $N^2 = J_p^2 = p J_p \equiv 0 \in M_p(\mathbb{F}_p)$.
        - Since $J_p \ne 0$, the minimal polynomial of $A$ is $m_A(x) = (x + 1)^2$.
        - Thus the largest Jordan block has size 2.
    <2>3. Geometric multiplicity:
        - All rows of $J_p$ are identical and non-zero, so $\operatorname{rank}(J_p) = 1$.
        - By Rank-Nullity, $\dim \ker(A + I_p) = \dim \ker(J_p) = p - 1$.
        - There are exactly $p - 1$ Jordan blocks for $\lambda = -1$.
    <2>4. Jordan block structure:
        - Since the partition of $p$ into $p - 1$ parts with largest part 2 is uniquely $2 + 1 + 1 + \dots + 1$, the JCF over $\mathbb{F}_p$ consists of one $2 \times 2$ block and $p - 2$ blocks of size $1 \times 1$:
        $$J_{\mathbb{F}_p}(A) = \begin{pmatrix}
        -1 & 1 & 0 & \cdots & 0 \\
        0 & -1 & 0 & \cdots & 0 \\
        0 & 0 & -1 & \cdots & 0 \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & 0 & \cdots & -1
        \end{pmatrix}.$$
    <2>5. Jordan basis and matrix $P$:
        - Choose the generalized eigenvector $w = e_1 = (1, 0, 0, \dots, 0)^t \in \mathbb{F}_p^p$.
        - Apply $A + I = J_p$:
        $$(A + I) w = J_p e_1 = (1, 1, \dots, 1)^t = v_1.$$
        - Since $(A + I) v_1 = J_p v_1 = p v_1 \equiv 0$, the pair $\{v_1, w\}$ forms a Jordan chain of length 2:
        $$A v_1 = -v_1, \qquad A w = v_1 - w.$$
        - For the remaining $p - 2$ blocks of size 1, choose eigenvectors $u_1, \dots, u_{p-2}$ where $u_i = e_1 - e_{i+1}$.
        - These $p$ vectors $\{v_1, w, u_1, u_2, \dots, u_{p-2}\}$ form a basis of $\mathbb{F}_p^p$.
        - Setting $P = \begin{pmatrix} v_1 & w & u_1 & u_2 & \cdots & u_{p-2} \end{pmatrix} \in \operatorname{GL}_p(\mathbb{F}_p)$ satisfies $P^{-1} A P = J_{\mathbb{F}_p}(A)$.

<1>4. Conclusion:
    *Proof:*
    Over $\mathbb{Q}$, $A$ is diagonalizable with eigenvalues $p-1$ (mult 1) and $-1$ (mult $p-1$). Over $\mathbb{F}_p$, $A$ has one Jordan block of size 2 and $p-2$ Jordan blocks of size 1 for eigenvalue $-1$.
:::
