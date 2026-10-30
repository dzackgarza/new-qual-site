# Algebra Qualifying Examination, Spring 2018

<a id="X508c21f16c7ba7bc7dd6068866ab1ca729539a1"></a>
## Instructions

Justify all the calculations and state the theorems you use in your answers. Each problem is worth 10 points.

<a id="problems"></a>
## Problems

1. Use the Class Equation (equivalently, the conjugation action of a group on itself) to prove that any $p$ -group (a group whose order is a positive power of a prime integer $p$ ) has a nontrivial center.
2. Prove that any group of order $p^{2}$  (where $p$  is prime) is abelian.
3. Prove that any group of order $5^{2}\cdot 7^{2}$  is abelian.
4. Write down exactly one representative in each isomorphism class of groups of order $5^{2}\cdot 7^{2}$ .

1. Let $f(x)=x^{4}-4x^{2}+2\mathbb{\in Q[}x]$ .

1. Find the splitting field $K$  of $f$ , and compute $[K\mathbb{:Q]}$ .
2. Find the Galois group $G$  of $f$ , both as an explicit group of automorphisms, and as a familiar abstract group to which it is isomorphic.
3. Exhibit explicitly the correspondence between subgroups of $G$  and intermediate fields between $\mathbb{Q}$  and $K$ .

2. Let $K$  be a Galois extension of $\mathbb{Q}$  with Galois group $G$ , and let $E_{1},E_{2}$  be intermediate fields of $K$  which are the splitting fields of irreducible $f_{i}(x\mathbb{)\in Q[}x]$ . Let $E=E_{1}E_{2}\subset K$ . Let $H_{i}=Gal(K/E_{i})$  and $H=Gal(K/E)$ .

1. Show that $H=H_{1}\cap H_{2}$ .
2. Show that $H_{1}H_{2}$  is a subgroup of $G$ .
3. Show that $Gal(K/(E_{1}\cap E_{2}))=H_{1}H_{2}$ .

3. Let

$$
A=\left[\begin{matrix}0&1&-2\\1&1&-3\\1&2&-4\end{matrix}\right]\in M_{3}\mathbb{(C)}
$$

1. Find the Jordan canonical form $J$  of $A$ .
2. Find an invertible matrix $P$  such that $P^{-1}AP=J$ . (You should not need to compute $P^{-1}$ .)

4. Let $M=\left(\begin{matrix}a&b\\c&d\end{matrix}\right)$  and $N=\left(\begin{matrix}x&u\\-y&-v\end{matrix}\right)$  over a commutative ring $R$ , where $b$  and $x$  are units of $R$ . Prove that if $MN=\left(\begin{matrix}0&0\\0&*\end{matrix}\right)$ , then $MN=0$ .
5. Let $M=\{(w,x,y,z)\in \mathbb{Z}^{4}\mid w+x+y+z\in 2\mathbb{Z\}}$ , and $N=\{(w,x,y,z)\in \mathbb{Z}^{4}\mid 4\mid (w-x), \hspace{0.25em} 4\mid (x-y), \hspace{0.25em} 4\mid (y-z)\}$ .

1. Show that $N$  is a $\mathbb{Z}$ -submodule of $M$ .
2. Find vectors $u_{1},u_{2},u_{3},u_{4}\in \mathbb{Z}^{4}$  and integers $d_{1},d_{2},d_{3},d_{4}$  such that $\{u_{1},u_{2},u_{3},u_{4}\}$  is a free basis for $M$ , and $\{d_{1}u_{1},d_{2}u_{2},d_{3}u_{3},d_{4}u_{4}\}$  is a free basis for $N$ .
3. Find vectors $u_{1},u_{2},u_{3},u_{4}\in \mathbb{Z}^{4}$  and integers $d_{1},d_{2},d_{3},d_{4}$  such that $\{u_{1},u_{2},u_{3},u_{4}\}$  is a free basis for $M$ , and $\{d_{1}u_{1},d_{2}u_{2},d_{3}u_{3},d_{4}u_{4}\}$  is a free basis for $N$ .
4. Use the previous part to describe $M/N$  as a direct sum of cyclic $\mathbb{Z}$ -modules.

6. Let $R$  be a PID and $M$  be an $R$ -module. Let $p$  be a prime element of $R$ . The module $M$  is called $\langle p\rangle$ -primary if for every $m\in M$  there exists $k>0$  such that $p^{k}m=0$ .

1. Suppose $M$  is $\langle p\rangle$ -primary. Show that if $m\in M$  and $t\in R$ , $t\notin \langle p\rangle$ , then there exists $a\in R$  such that $atm=m$ .
2. A submodule $S$  of $M$  is said to be pure if $S\cap rM=rS$  for all $r\in R$ . Show that if $M$  is $\langle p\rangle$ -primary, then $S$  is pure if and only if $S\cap p^{k}M=p^{k}S$  for all $k\geq 0$ .

7. Let $R=C[0,1]$  be the ring of continuous real-valued functions on the interval $[0,1]$ . Let $I$  be an ideal of $R$ .

1. Show that if $f\in I$ , $a\in [0,1]$  are such that $f(a)\ne 0$ , then there exists $g\in I$  such that $g(x)\geq 0$  for all $x\in [0,1]$ , and $g(x)>0$  for all $x$  in some open neighborhood of $a$ .
2. If $I\ne R$ , show that the set $Z_{I}=\{x\in [0,1]\mid f(x)=0, \hspace{0.25em} all f\in I\}$  is nonempty.
3. Show that if $I$  is maximal, then there exists $x_{0}\in [0,1]$  such that $I=\{f\in R\mid f(x_{0})=0\}$ .