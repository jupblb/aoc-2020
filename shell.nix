{ pkgs ? import <nixpkgs> {} }:

let python-with-packages = pkgs.python37.withPackages(ps: with ps; [
  python-language-server
]);
in pkgs.mkShell {
  buildInputs = [ python-with-packages ];
}
