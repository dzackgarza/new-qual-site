# Qualifying Exam: Complex Analysis — Spring 2014

Committee: Ed Azoff, Sa’ar Hersonsky (Chair) and Jingzhi Tie

<a id="instructions"></a>
## Instructions

Give clear reasoning. State clearly which theorems you are using. You should not cite anything else: examples, exercises, or problems. Cross out the parts you do not want to be graded. Read through all the problems, do them in any order, the one you feel most confident about first. They are not in order of difficulty. Each question weights equally.

<a id="problems"></a>
## Problems

1. Let $f$  be a continuous function in the region

$$
D=\{z\mid |z|>1, \hspace{0.25em} 0\leq argz\leq \theta \} \quad where \quad 0\leq \theta \leq 2\pi .
$$

- Suppose that there exists $k$  such that $lim_{z\rightarrow \infty }zf(z)=k$  for $z$  in the region $D$ . Show that

$$
\lim_{R\to \infty }\int_{L}^{​}f(z) \, dz=i\theta k,
$$

- where $L$  is the part of the circle $|z|=R$  which lies in the region $D$ .

2. Use methods of complex variables to evaluate the integral

$$
\int_{-\infty }^{\infty }\frac{sinx}{x} \, dx.
$$

1. Assume the infinite series $\sum_{n=0}^{\infty }c_{n}z^{n}$  converges in $|z|<R$  and let $f(z)$  be the limit. Show that for $r<R$ ,

$$
\frac{1}{2\pi }\int_{0}^{2\pi }\left|f​\left(re^{i\theta }\right)\right|^{2}d\theta =\sum_{n=0}^{\infty }|c_{n}|^{2}r^{2n}.
$$

2. Deduce Liouville's theorem from (a). Liouville's theorem: If $f(z)$  is entire and bounded, then $f$  is constant.

3. Apply Rouché's Theorem to prove the Fundamental Theorem of Algebra: If

$$
P(z)=a_{0}+a_{1}z+\cdots +a_{n-1}z^{n-1}+a_{n}z^{n} \quad \quad (a_{n}\ne 0)
$$

- is a polynomial of degree $n>0$ , then it has a zero in $\mathbb{C}$ .

4. Suppose $\mathscr{l}$  is a line and $C$  is a circle in the plane. Under what conditions is there a Mobius map which simultaneously sends $\mathscr{l}\cup \{\infty \}$  and $C$  to concentric circles? Justify your conclusions.
5. Let $g$  be analytic for $|z|<1$  and $|g(z)|<1$  for $|z|<1$ . Prove that if $g$  has more than one fixed point in $|z|<1$ , then $g$  must be the identity function.

- (For partial credit, you may assume that $g$  is actually analytic on $|z|\leq 1$  with $|g(z)|<1$  for $|z|=1$ .)

6. Suppose $f$  has an isolated singularity at $a\mathbb{\in C}$  and $\mathfrak{R}f$  is bounded above in a deleted neighborhood of $a$ . Prove that the singularity is removable.