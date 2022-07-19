"""Insta user"""
from __future__ import annotations

from typing import List, Dict


class InstaUser:
    """Instagram User Project."""
    username: str
    password: str
    followers: List[str]
    following: List[str]

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.followers = []
        self.following = []

    def getFollowerCount(self) -> int:
        num_followers = len(self.followers)
        return num_followers

    def getFollowingCount(self) _> int:
        num_following = len(self.following)
        return num_following

    def getMutuals(self) -> List[str]:
        mutual: List[str] = []
        for i in range(0, len(self.followers)):
            for j in range (0, len(self.following)):
                if self.followers[i] == self.followers[j]:
                    mutual.append(self.followers[i])
        return mutual
    
    def follow(self, person: InstaUser) -> None:
        self.following.append(person.username)
        person.addFollower(self)

    def addFollower(self, person: InstaUser) -> None:
        self.followers.append(person.username)

    
        


class Student:

    name: str
    schedule: Dict[str, str]
    credit_hours: int
    full_time: bool

    def __init__(self, name: str, status: bool):
        self.name = name
        self.full_time = status
        self.credit_hours = 0
        self.schedule = {}

    def add_course(self, course: str, time: str, credits: int) -> None:
        if self.full_time == True:
            if self.credit_hours + credits > 18:
                print("Add unsuccesful: too many credit hours")
            else:
                if course in self.schedule:
                    self.schedule[course] = time



    