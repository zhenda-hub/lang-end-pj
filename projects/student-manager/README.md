# 学生信息管理系统

一个基于控制台的学生成绩管理应用。

## 概述

本项目是一个完整的学生信息管理系统，支持对学生信息的增删改查、排序和备份功能。数据持久化存储在本地文件中。

## 涵盖知识点

- 数据结构的使用（列表、字典等）
- 文件读写操作
- 用户输入处理
- 字符串操作
- 排序算法
- 异常处理
- 函数封装与模块化

## 主要功能

- 添加学生信息（学号、姓名、各科成绩）
- 查询学生信息（按学号或姓名）
- 删除学生记录
- 修改学生信息
- 按科目排序（升序/降序）
- 显示所有学生信息
- 统计学生数量
- 数据备份

## 运行方式

### Python 版本
```bash
cd projects/student-manager/python
python demo.py
```

### Go 版本
（计划中）

### TypeScript 版本
（计划中）

## 数据存储

数据文件存储在各语言实现的 `data/` 目录下：
- Python: `projects/student-manager/python/data/student.txt`
- Go: `projects/student-manager/go/data/`
- TypeScript: `projects/student-manager/typescript/data/`

## 语言实现对比

| 特性 | Python | Go | TypeScript |
|------|--------|-----|------------|
| 状态 | ✅ 已实现 | 🚧 计划中 | 🚧 计划中 |
