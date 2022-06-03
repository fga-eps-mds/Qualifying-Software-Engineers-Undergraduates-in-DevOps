# Ebook

Para rodar este livro localmente, há de se instalar Rust (e Cargo) no seu sistema.

* [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install)

Então, basta instalar a crate [mdBook](https://github.com/rust-lang/mdBook):

```bash
cargo install mdbook
```

Por fim, a partir da pasta raiz deste repositório, basta rodar

```bash
mdbook serve
```

E acessar o [localhost](http://localhost:3000/) :)