let
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python3Packages.pip
    python3Packages.virtualenv
    git
    gnumake
    bash
  ];

  shellHook = ''
    if [ ! -d venv ]; then
      echo "Creando virtualenv..."
      python3 -m venv venv
    fi
    source venv/bin/activate
  '';
}