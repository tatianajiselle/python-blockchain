#!/usr/bin/env python3


class Block:
  def __init__(self, index, hash_, previous_hash, timestamp, data) : 
    self.index = index
    self.hash = hash_
    self.previous_hash = previous_hash
    self.timestamp = timestamp
    self.data = data


