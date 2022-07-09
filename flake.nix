{
  description = "valorant utils";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (system:
      let pkgs = nixpkgs.legacyPackages.${system};
      in
      rec {

        # Use nixpkgs-fmt for `nix fmt'
        formatter = pkgs.nixpkgs-fmt;

        defaultPackage = packages.valorant-utils;

        packages = flake-utils.lib.flattenTree rec {

          valorant-utils = with pkgs.python310Packages;
            buildPythonPackage rec {
              pname = "valorant-utils";
              version = "0.2.0";

              src = self;
              propagatedBuildInputs = [
                requests
              ];

              doCheck = false;
              pythonImportsCheck = [
                "valorant"
              ];

              meta = with pkgs.lib; {
                description = "valorant utils";
                homepage = "https://github.com/make-or-break/valorant-utils/";
                platforms = platforms.unix;
                maintainers = with maintainers; [ mayniklas ];
              };
            };

        };

      });
}
