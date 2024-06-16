#!/bin/bash

# Install Fuel toolchain
curl --proto '=https' --tlsv1.2 -sSf https://fuelup.dev | sh
fuelup self update

# Install Rust toolchain
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup update
