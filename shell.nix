{ pkgs ? import <nixpkgs> {} }:

let python-with-packages = pkgs.python3.withPackages(ps: []);
in pkgs.mkShell {
  buildInputs = [ python-with-packages ];
}
