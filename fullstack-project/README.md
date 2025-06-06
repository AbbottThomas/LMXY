# LMXY

## 第二版本目的

- 项目环境重构
  - 多个pixi项目变成一个pixi项目
  - 再细分成前端，后端，生产虚拟环境
  - 每个虚拟环境，保持基础包的一致性，保持功能开关
  - 前端，后端项目文件，都含有学习用的文件夹
- 分支流程重构
  - main，正式版本
  - devlop，开发版本
  - temp，临时模块
  - bug，调式bug
- Web多应用综合，初步完成demo
  - 业务核心功能
  - 调试和日志信息
  - 单元测试，集成测试，端点测试，负载测试，生产部署
- CI/CD， GitHub Action,    (Jenkins负载，强大，日后学)
  - 持续集成，集成交付
  - 代码提交触发CI，自动化完成
    - 运行构建，多层次测试，代码质量检测，构建镜像，推送镜像
    - 触发CD工具,  部署到服务器（Nginx,Uvicorn,Kubernetes）
    - 回滚机制
- 运维相关
  - ELK Stack（Elasticsearch + Logstash + Kibana）：日志收集、存储与可视化
  - Prometheus/Grafana,用于监控和可视化应用性能
  - Velero：Kubernetes集群的备份与恢复工具
  - Wazuh：功能全面，开源免费的安全监控和入侵检测平台

## 第三版本目的
- 
